from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='E-mail',required=True)
    class Meta():
        model = User
        fields = ('username','email','first_name','last_name','password1','password2')

class UserProfileChangeForm(UserChangeForm):
    class Meta():
        model = User
        fields = ('username','email','first_name','last_name','password')

class ProfilePicChangeForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ['profile_pic',]
