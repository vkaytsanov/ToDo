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
    return render(request, 'index.html', args)
