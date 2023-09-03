from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Genre
from django.contrib import messages
from .forms import GenreCreateForm ,GenreUpdateForm
from django.views import View
# Create your views here.



class HomeView(View):

    def get(self, request):
        all = Genre.objects.all()
        return render(request , 'home/home.html' , {'all': all})

    def post(self, request):
        all = Genre.objects.all()
        return render(request , 'home/home.html' , {'all': all})


class DetailView(View ):
    def get(self, request , genre_id):
        genre = Genre.objects.get(id=genre_id)
        return render(request , 'home/detail.html', {'genre':genre})       


class DeleteView(View):
    def get(self, request , genre_id):
        Genre.objects.get(id=genre_id).delete()
        messages.success(request ,"Genre deleted" , 'success')
        return redirect('home:home')





def create(request):
    if request.method == 'POST':
        form = GenreCreateForm(request.POST)
        if form.is_valid ():
            cd = form.cleaned_data
            Genre.objects.create(name=cd['name'] , description = cd['description'] ,  created = cd['created'])
            messages.success(request , 'Genre created successfully')
            return redirect('home:home')
    else:
        form = GenreCreateForm()
    return render(request, 'create.html', {'form': form})


def update(request , genre_id):
    genre = Genre.objects.get(id=genre_id)
    if request.method == 'POST':
        form = GenreUpdateForm(request.POST ,instance=genre)
        if form.is_valid():
            form.save()
            messages.success(request ,'update completed successfully' , 'success' )
            return redirect ('details' , genre_id)
    else:
        form = GenreUpdateForm(instance=genre)
    return render(request, 'update.html', {'form': form})