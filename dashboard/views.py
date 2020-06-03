from django.shortcuts import render, redirect
from core.functions.user_handling import hashFunction
from django.utils import timezone

# Create your views here.
from core.models import Note, User


def index(request):
    if 'name' not in request.session:
        return redirect('../', {})
    cur_user = User.objects.get(username=request.session['name'])
    if request.method == "POST":
        if 'note_id' in request.POST:
            note = Note.objects.filter(id=request.POST['note_id']).get()
            note.is_visible = False
            note.save()
        else:
            note_title = request.POST['note_title']
            if len(note_title) > 0:
                note = Note(user_id=cur_user, description=note_title, date_created=timezone.now().date(),
                            date_expected=timezone.now().date(),
                            is_completed=False, is_visible=True, joined_users='')
                note.save()
    user_notes = []
    for note in Note.objects.filter(user_id=cur_user.getId()):
        if note.is_visible != '0':
            user_notes.append(note)
    return render(request, 'dashboard/index.html', {'user_notes': user_notes})


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
