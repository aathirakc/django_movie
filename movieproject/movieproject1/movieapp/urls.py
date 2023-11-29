
from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='movieapp.home'),
    path('movie_names/<int:id>/',views.movie_names,name='movieapp.movie_names'),
    path('add/',views.add,name='movieapp.add'),
    path('update/<int:id>/',views.update,name='movieapp.update'),
    path('delete/<int:id>/',views.delete,name='movieapp.delete'),
]
