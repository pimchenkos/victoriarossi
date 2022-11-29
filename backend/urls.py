from django.urls import path
from . import views

urlpatterns = [
    path('api/main', views.MainCreate.as_view()),
]
