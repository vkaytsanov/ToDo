
from django.contrib.auth.forms import UserCreationForm, forms

from core.models import User


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

    def save(self, commit=True):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password1']

        user = User(username=username, email=email, password=password)
        if commit:
            user.save()
        return user
