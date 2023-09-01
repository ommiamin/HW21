from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    return HttpResponse('say hello')

def home(request):
    return HttpResponse('home')
