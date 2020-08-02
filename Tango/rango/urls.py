from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns  = [
    path('home/', views.homeview, name = 'Home'),
    path('about/', views.aboutview, name = 'about'),
    path('info/', views.infoview, name = 'info'),

]