from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns  = [
    path('', views.homeview, name = 'Home'),
    path('home/', views.homeview, name = 'Home'),
    path('about/', views.aboutview, name = 'About'),
    path('info/', views.infoview, name = 'Info'),

]