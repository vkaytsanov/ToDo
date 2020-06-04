from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect

from core.functions.user_handling import handleRegistration, hashFunction, login, handleEmailSend
from core.models import User

''' we call the render function with the following request on the page we would like to render,
    the 3rd parameter is for passing variables with values, which can be used, type {} for none
'''

"""  get count of registered users from the database """


def index(request):
    args = {}
    number_of_registered = 700 + User.objects.count()
    args['number_of_registered'] = number_of_registered
    return render(request, 'landing_page/index.html', args)


def signin(request):
    args = {}
    if 'name' in request.session:
        return redirect('../dashboard/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        response, message = login(username, password)
        if response:
            request.session['name'] = username
            return redirect('../dashboard/', {'args': args})
        else:
            args['response_message'] = message
            return render(request, 'landing_page/login.html', {'args': args})
    else:
        return render(request, 'landing_page/login.html', {'args': args})


def register(request):
    args = {}
    if request.method == "POST":
        response, message = handleRegistration(request.POST)
        if response:
            password = hashFunction(request.POST['password'])
            user = User(username=request.POST['username'], email=request.POST['email'], password=password)
            user.save()
            args['response_message'] = 'Успешно създаване на акаунт'
            request.session['name'] = user.getUsername()
            return render(request, 'dashboard/index.html', {'args': args})
        else:
            args['response_message'] = message

    return render(request, 'landing_page/register.html', {'form': args})


def about(request):
    return render(request, 'landing_page/about.html', {})


def contact(request):
    args = {}
    if request.method == 'POST':
        response = handleEmailSend(request.POST)
        args['response_message'] = response
    return render(request, 'landing_page/contact.html', {'args': args})


def privacy_policy(request):
    return render(request, 'landing_page/privacy-policy.html', {})
