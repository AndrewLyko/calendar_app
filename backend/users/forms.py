from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from users.models import UserDetail, User


class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)

    def save(self):
        pass


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self, commit=True, *args, **kwargs):
        m = super().save(commit=False)

        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()

        return m


class UserDetailsForm(forms.ModelForm):
    lastname = forms.CharField(required=False)

    class Meta:
        model = UserDetail
        fields = ['firstname', 'lastname', 'username', 'email']

    def clean_firstname(self):  # metoda do walidacji
        name = self.cleaned_data.get('firstname')
        if not name.isalpha():
            raise ValidationError('10 years-old and three kids? Come on')
        return name
