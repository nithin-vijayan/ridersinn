from userprofile.models import Profile,Post
from django.contrib.auth.forms import PasswordChangeForm,UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fullname','bio', 'location', 'birth_date','avatar')


    def clean_fullname(self):
        fullname = self.cleaned_data.get('fullname')
        if fullname:
            return fullname
        raise forms.ValidationError(u'Fullname is required')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('postcontent',)
