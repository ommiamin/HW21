from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('', views.HomeView.as_view() , name='home'),
    path('detail/<int:genre_id>' , views.DetailView.as_view() , name='details') ,
    path('delete/<int:genre_id>' , views.DeleteView.as_view() , name='delete'),
    path('update/<int:genre_id>' , views.update , name='update'),
    path('create/' , views.create , name='create'),
]
