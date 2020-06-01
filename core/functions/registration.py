from core.models import User
import re

users = User.objects.all()


def handleRegistration(POST):
    username = POST['username']
    email = POST['email']
    password = POST['password']
    repeat_password = POST['repeat_password']
    print(username)
    print(email)
    print(password)
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

    for user in users:
        if username == user.getUsername():
            return False, "Потребителското име вече е заето, да не би да сте си забравили данните?"
    return True, ""


def checkValidEmail(email):
    if len(email) == 0:
        return False, "Трябва да въведете имейл"
    if len(email) < 3:
        return False, "Имейлът е твърде къс"
    for user in users:
        if email == user.getEmail():
            return False, "Такъв имейл вече съществува, да не би да сте си забравили данните?"
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
    if not bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})', password)):
        return False, "Паролата е твърде лесна"
    if password is not repeat_password:
        return False, "Въведените пароли не съвпадат"
    return True, ""
