from django.shortcuts import render, redirect
from core.functions.user_handling import hashFunction
from django.utils import timezone

# Create your views here.
from core.models import Note, User


def index(request):
    notes_by_category = {}
    if 'name' not in request.session:
        return redirect('../', {})
    cur_user = User.objects.get(username=request.session['name'])
    if request.method == "POST":
        if 'new_category' in request.POST:
            note_category = request.POST['new_category'].rstrip(" ")
            note = Note(user_id=cur_user, category=note_category, description='placeholder', is_visible=False,
                        joined_users='')
            note.save()
        elif 'note_id' in request.POST:
            note = Note.objects.filter(id=request.POST['note_id']).get()
            note.is_visible = False
            note.save()
        elif 'add' in request.POST:
            note_title = request.POST['note_title']
            note_category = request.POST['note_category'].rstrip(" ")
            if len(note_title) > 0:
                try:
                    note = Note(user_id=cur_user, category=note_category,
                                description=note_title, is_visible=True, joined_users='')
                    note.save()
                except Exception:
                    pass
        elif 'close-category' in request.POST:
            print(request.POST['cat'])
            notes = Note.objects.filter(user_id=cur_user.getId(), category=request.POST['cat'])
            notes.delete()

    for note in Note.objects.filter(user_id=cur_user.getId()):
        cat = str(note.category).strip(" ")
        try:
            notes_by_category[cat]
        except KeyError:
            notes_by_category[cat] = []
        finally:
            if bool(note.is_visible):
                notes_by_category[cat].append(note)
    can_add_category = True
    if len(notes_by_category.keys()) > 4:
        can_add_category = False
    return render(request, 'dashboard/index.html', {'user_notes': notes_by_category, 'add_additional': can_add_category})


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
    args['note_count_successful'] = Note.objects.filter(user_id=user.getId(), is_visible=False).count()
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
