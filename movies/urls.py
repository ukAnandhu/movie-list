from django.urls import path

from movies import views

urlpatterns = [

    path('', views.movie_list, name='movie_list'),
    path('movies/<int:id>/',views.details,name='details'),
    path('search/',views.search,name='search'),
    path('add_movie/',views.add_movie,name='add_movie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),


]
