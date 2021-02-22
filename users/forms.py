from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Profile

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField(max_length=120)
    password=forms.CharField(max_length=120)
    def clean(self):
        print("inside clean validate username and password")

class ProfileCreateForm(ModelForm):
    user=forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model=Profile
        fields=["user","profile_pic","bio","birth_date"]


