from django import forms 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class UserRegisterationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs= {'class': 'form-control','placeholder':'your username',}))
    email = forms.EmailField(widget=forms.EmailInput(attrs= {'class': 'form-control','placeholder':'your Email',}))
    password1 = forms.CharField(label='password' ,widget=forms.PasswordInput(attrs= {'class': 'form-control','placeholder':'your password',}))
    password2= forms.CharField(label='confirm password' ,widget=forms.PasswordInput(attrs= {'class': 'form-control','placeholder':'your password',}))


    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This Email is already exists')
        return email
    
    def clean(self):
        cd = super().clean()
        p1=cd.get('password1')
        p2=cd.get('password2')

        if p1 and p2 and p1 != p2:
            raise ValidationError('password and confirm password must be the same')

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs= {'class': 'form-control','placeholder':'your username',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs= {'class': 'form-control','placeholder':'your password',}))
