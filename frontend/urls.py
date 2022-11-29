from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutMe', views.aboutMe, name='aboutMe'),
    path('services', views.services, name='services'),
    path('news', include('news.urls')),
    path('contacts', views.contacts, name='contacts'),
    path('clients', views.clients, name='clients'),

]
