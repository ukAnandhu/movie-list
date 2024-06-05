from django.urls import path

from movies import views

urlpatterns = [
    path('', views.fetch_data, name='fetch_data'),

    # path('movie/', views.movie_list, name='movie_list'),
    path('movies/<int:id>/',views.details,name='details'),
    path('search/',views.search,name='search'),
]
