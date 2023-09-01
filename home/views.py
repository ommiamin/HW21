from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Genre
# Create your views here.


def home(request):
    all = Genre.objects.all()
    return render(request , 'home.html' , {'all': all})

def detail(request , genre_id):
    genre = Genre.objects.get(id=genre_id)
    return render(request , 'detail.html', {'genre':genre})

def delete(request ,genre_id):
    Genre.objects.get(id=genre_id).delete()
    return redirect('home')