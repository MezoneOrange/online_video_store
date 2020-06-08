from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class UserOurRegistration(UserCreationForm):
    email = forms.EmailField(required=True)  # required определяет обязательный ли этот параметр

    class Meta:  # определяет каким образом мы будем взаимодействовать с какой-либо табличкой
        model = User  # таблица SQL с которой мы работаем
        fields = ['username', 'password1', 'password2', 'email']  # последовательнось расположения полей


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields['image'].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ['image']
