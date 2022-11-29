from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserChangeForm, CustomUserCreationForm
# from .models import CustomUser
from .models import Profile, ImageProfile


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username', 'first_name', 'last_name']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("User", "PhoneNumber")


@admin.register(ImageProfile)
class ImageProfileAdmin(admin.ModelAdmin):
    list_display = ("User", "image")


# admin.site.register(CustomUser, CustomUserAdmin)
