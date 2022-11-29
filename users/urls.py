from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('session/', views.get_session, name='get_session'),
    path('captcha/', include('captcha.urls'))
]
