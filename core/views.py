from django.http import HttpResponse
from django.shortcuts import render

''' we call the render function with the following request on the page we would like to render,
    the 3rd parameter is for passing variables with values, which can be used, type {} for none
'''

""" ToDo get count of registered users from the database """


def index(request):
    args = {}
    number_of_registered = 13000
    args['number_of_registered'] = number_of_registered
    return render(request, 'landing_page/index.html', args)


def login(request):
    return render(request, 'landing_page/login.html', {})


def register(request):
    return render(request, 'landing_page/register.html', {})


def about(request):
    return render(request, 'landing_page/about.html', {})


def contact(request):
    return render(request, 'landing_page/contact.html', {})


def privacy_policy(request):
    return render(request, 'landing_page/privacy-policy.html', {})