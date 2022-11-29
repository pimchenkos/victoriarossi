from django import forms
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User
from .models import Profile, ImageProfile
from allauth.account.forms import SignupForm
from captcha.fields import CaptchaField


# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ('email',)
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = UserChangeForm.Meta.fields


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name']


class Profile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        self.fields['PhoneNumber'].label = "Телефон"

    class Meta:
        model = Profile
        fields = ['PhoneNumber']


class ImageProfile(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImageProfile, self).__init__(*args, **kwargs)
        self.fields['image'].label = "Изображение"

    class Meta:
        model = ImageProfile
        fields = ['image']


class SignUp(SignupForm):
    captcha = CaptchaField(label='Введите символы с картинки:')
