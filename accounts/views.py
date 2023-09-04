from django.shortcuts import render ,redirect
from .forms import  UserRegisterationForm ,UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login ,logout
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class UserRegisterView(View):
    form_class= UserRegisterationForm
    template_name='accounts/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            print(cd)
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            messages.success(request , "User registration successful" , "Success")
            return redirect('home:home')
        return render(request, self.template_name , {"form": form}) #this is for error that dont complete the form


class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request ):
        form = self.form_class()#make instance from class
        return render(request, self.template_name, {"form": form})

    def post(self, request ):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(request , username=cd['username'] ,password=cd['password'])
            if user is not None :
                login(request , user)# user in request
                messages.success(request , "User Login successful" , "Success")
                return redirect('home:home')
            else:
                messages.error(request , "username or password incorrect" , 'danger')

        return render(request, self.template_name, {"form": form})



class UserLogoutView(LoginRequiredMixin ,  View):
    def get(self, request):
        logout(request)
        messages.success(request , 'logged out successfully ' ,'success')
        return redirect('home:home')




class UserProfileView(LoginRequiredMixin , View):
    def get(self, request , user_id):
        print(user_id)
        user=User.objects.get(id=user_id)
        
        return render(request , 'accounts/profile.html',{'user':user})