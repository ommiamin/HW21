from django.urls import path
from . import views

urlpatterns = [
    path('',views.home , name='home'),
    path('detail/<int:genre_id>' , views.detail , name='details') ,
    path('delete/<int:genre_id>' , views.delete , name='delete'),
    path('update/<int:genre_id>' , views.update , name='update'),
    path('create/' , views.create , name='create'),
]
