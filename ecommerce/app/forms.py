from django import forms
from .models import *
from . forms import *
from django.contrib.auth.forms import UserCreationForm
# class UserForm(forms.ModelForm):
#     class Meta:
#         model=UserModel
#         fields=['Fullname','username','email','password','password2','phone','picture']
#         widgets={
#             'password':forms.PasswordInput(),
#             'password2':forms.PasswordInput()
#         }

class UserForm(UserCreationForm):
    class Meta:
        model=UserModels
        fields=['Fullname','phone','email']
       

# class IdentifyForm(forms.ModelForm):
#     class Meta:
#         models=UserModels
#         fields=['username']
    