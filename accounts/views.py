from django.shortcuts import render ,redirect
from .forms import  UserRegisterForm ,UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'],cd['password'])
            messages.success(request , "User registration successful" , "Success")
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {"form": form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(request , username=cd['username'] ,password=cd['password'])
            if user is not None :
                login(request , user)
                messages.success(request , "User Login successful" , "Success")
                return redirect('home')
            else:
                messages.error(request , "username or password incorrect" , 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form": form})