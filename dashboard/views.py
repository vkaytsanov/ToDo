from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    if 'name' not in request.session:
        return redirect('../', {})
    return render(request, 'dashboard/index.html', {})


def logout(request):
    try:
        del request.session['name']
    except KeyError:
        return render(request, 'dashboard/logout.html', {})
    return render(request, 'dashboard/logout.html', {})
