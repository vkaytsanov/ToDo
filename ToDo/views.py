from django.http import HttpResponse
from django.shortcuts import render

''' we call the render function with the following request on the page we would like to render,
    the 3rd parameter is for passing variables with values, which can be used, type {} for none
'''


def index(request):
    return render(request, 'index.html', {})
