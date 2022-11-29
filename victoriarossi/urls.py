"""victoriarossi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from allauth.account.views import ConfirmEmailView, EmailVerificationSentView
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('', include('backend.urls')),
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include("allauth.urls")),
    path('accounts/profile/', include('users.urls')),
    # Auth API
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/register/account-email-verification-sent/', EmailVerificationSentView.as_view(),
         name='account_email_verification_sent', ),
    path('api/auth/register/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(),
         name='account_confirm_email'),
    path('api/auth/register/', include('dj_rest_auth.registration.urls')),
    # Schema API
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI API:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Django CKEditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
