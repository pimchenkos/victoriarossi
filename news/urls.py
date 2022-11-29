from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='news'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('add/', views.CreateNewsView.as_view(), name='news-add'),
    path('<int:pk>/update/', views.UpdateNewsView.as_view(), name='news-update'),
    path('<int:pk>/delete/', views.DeleteNewsView.as_view(), name='news-delete'),
]
