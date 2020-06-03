from django.shortcuts import redirect
from django.core.mail import send_mail
from core.models import User
import re
from hashlib import sha256

users = User.objects.all()


def login(username, password):
    for user in users:
        if username == user.getUsername():
            if hashFunction(password) == user.getPassword():
                return True, ""
            else:
                return False, "Невалидна парола"
    return False, "Такъв потребител не съществува"


def hashFunction(password):
    hashed = sha256(password.encode('utf-8'))
    hex = hashed.hexdigest()
    return hex


def handleRegistration(POST):
    username = POST['username']
    email = POST['email']
    password = POST['password']
    repeat_password = POST['repeat_password']
    check, message = checkValidUsername(username)
    if not check:
        return check, message
    check, message = checkValidEmail(email)
    if not check:
        return check, message
    check, message = checkValidPassword(password, repeat_password)
    return check, message


def checkValidUsername(username):
    if len(username) == 0:
        return False, "Трябва да въведете потребителско име"
    if len(username) < 3:
        return False, "Потребителското име е твърде късо"

    if User.objects.filter(username=username).count() == 1:
        return False, "Потребителското име вече е заето, да не би да сте си забравили данните?"
    return True, ""


def checkValidEmail(email):
    if len(email) == 0:
        return False, "Трябва да въведете имейл"
    if len(email) < 3:
        return False, "Имейлът е твърде къс"
    if User.objects.filter(email=email).count() == 1:
        return False, "Такъв имейл вече съществува, да не би да сте си забравили данните?"
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        return True, ""
    return False, "Имейл адресът не е валиден."


def handleEmailSend(POST):
    name = POST['first-name']
    email = POST['email']
    message = POST['message']
    check, response_message = checkNotSpamName(name)
    if not check:
        return response_message
    check, response_message = checkNotSpamEmail(email)
    if not check:
        return response_message
    check, response_message = checkNotSpamMessage(message)
    if check:
        send_mail(
            '[Reminders] Мейл от ' + name,
            message,
            email,
            ['vkaytsanov@yahoo.com'],
            fail_silently=False,
        )
        return 'Успешно ни изпратихте съобщение. Ще се свържем с вас възможно най-скоро!'
    return response_message


def checkNotSpamName(name):
    if len(name) == 0:
        return False, "Моля, въведете вашето име"
    return True, ""


def checkNotSpamMessage(message):
    if len(message) == 0:
        return False, "Моля, въведете вашето съобщение"
    SPAM_KEYWORDS = ['viagra', 'sex', 'toys', 'SEO', 'course', 'growth', 'Verdiеnеn', 'ЖАРКАЯ ШТУЧКА', 'Dаting',
                     'Germany', 'girls']
    for keyword in SPAM_KEYWORDS:
        for word in message.split():
            if word in keyword:
                return False, "Успешно изпратихте вашето съобщение :)"

    return True, ""


def checkNotSpamEmail(email):
    if len(email) == 0:
        return False, "Трябва да въведете имейл"
    if len(email) < 3:
        return False, "Имейлът е твърде къс"
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        return True, ""
    return False, "Имейл адресът не е валиден."


def checkValidPassword(password, repeat_password):
    if len(password) == 0:
        return False, "Трябва да въведете парола"
    if len(repeat_password) == 0:
        return False, "Трябва да повторите въведената парола"
    if len(password) < 6:
        return False, "Трябва да въведете парола по дълга от 6 символа"
    if password != repeat_password:
        return False, "Въведените пароли не съвпадат"
    return True, ""
