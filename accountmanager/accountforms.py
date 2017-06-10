from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import DateInput

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email


class passwordResetForm(PasswordChangeForm):
    pass
