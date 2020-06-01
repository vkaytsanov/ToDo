from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from core.functions.registration import handleRegistration
from core.forms import RegistrationForm
from core.models import User

''' we call the render function with the following request on the page we would like to render,
    the 3rd parameter is for passing variables with values, which can be used, type {} for none
'''

""" ToDo get count of registered users from the database """


def index(request):
    args = {}
    number_of_registered = 13000
    args['number_of_registered'] = number_of_registered
    return render(request, 'landing_page/index.html', args)


def signin(request):
    return render(request, 'landing_page/login.html', {})


def register(request):
    args = {}
    if request.method == "POST":
        response, message = handleRegistration(request.POST)
        if response:
            user = User(request.POST['username'], request.POST['email'], request.POST['password'])
            user.save()
            args['response'] = True
            args['response_message'] = 'Успешно създаване на акаунт'
        else:
            args['response'] = False
            args['response_message'] = message

    return render(request, 'landing_page/register.html', {'form': args})


def registered_users(request):
    users = User.objects.all()
    print(users)
    return render(request, 'landing_page/registered-users.html', {'users': users})


def about(request):
    return render(request, 'landing_page/about.html', {})


def contact(request):
    return render(request, 'landing_page/contact.html', {})


def privacy_policy(request):
    return render(request, 'landing_page/privacy-policy.html', {})
