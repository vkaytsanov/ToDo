from django.shortcuts import render, redirect
from core.functions.user_handling import hashFunction


# Create your views here.
from core.models import Note, User


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


def profile(request):
    args = {}
    user = User.objects.get(username=request.session['name'])
    args['note_count'] = Note.objects.filter(user_id=user.getId()).count()
    if request.method == 'POST':
        get_password = request.POST['password']
        new_password = hashFunction(get_password)
        if user.password != new_password:
            user.password = new_password
            args['password_response'] = 'Успешно сменихте паролата си.'
            user.save()
        else:
            args['password_response'] = 'Възникна грешка, моля, опитайте пак.'

    return render(request, 'dashboard/profile.html', {'args': args})
