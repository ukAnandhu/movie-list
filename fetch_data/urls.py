

from django.urls import path

from fetch_data import views


urlpatterns = [

    path('', views.fetch_data, name='fetch_data'),

]