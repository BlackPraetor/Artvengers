from django.contrib.auth import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields


class SignupForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'class': 'form-control rounded-pill','placeholder': 'Email'}))
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control rounded-pill','placeholder': 'Username'}),help_text="")
    password1 = forms.CharField(label="",help_text="",max_length=20,widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill','type':'password','placeholder': 'Password'}))
    password2 = forms.CharField(label="",help_text="",max_length=20,widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill','type':'password','placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ('email','username','password1','password2')


    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)



class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput())
    email = forms.EmailField(max_length=100,widget=forms.TextInput())

    class Meta:
        model = User
        fields = ('username','email','password')


class ChangePasswordForm(PasswordChangeForm):
    new_password1 = forms.CharField(label="",help_text="",max_length=100,widget=forms.PasswordInput(attrs={'type':'password'}))
    new_password2 = forms.CharField(label="",help_text="",max_length=100,widget=forms.PasswordInput(attrs={'type':'password'}))


    class Meta:
        model = User
        fields = ('new_password1','new_password2')