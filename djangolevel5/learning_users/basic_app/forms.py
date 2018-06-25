from django.forms import ModelForm
from django import forms
from basic_app.models import UserProfInfo
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


#class UserProfInfoform(forms.ModelForm):
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfInfo
        fields = ('portfolio_site','profile_pic')
