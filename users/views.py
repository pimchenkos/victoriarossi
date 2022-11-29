from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .forms import Profile, ImageProfile, UserUpdateForm
from django.http import JsonResponse


@login_required
def profile(request):
    if request.method == "POST":
        user_profile = Profile(request.POST, instance=request.user.profile)
        image_profile = ImageProfile(request.POST, request.FILES, instance=request.user.imageprofile)
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid() and user_profile.is_valid() and image_profile.is_valid():
            update_user.save()
            user_profile.save()
            image_profile.save()
            messages.success(request, f'Данные профиля успешно обновлены')
            return redirect('profile')
    else:
        user_profile = Profile(instance=request.user.profile)
        image_profile = ImageProfile(instance=request.user.imageprofile)
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'profile': user_profile,
        'imageProfile': image_profile,
        'update_user': update_user
    }
    return render(request, "users/profile.html", data)


@api_view(['GET', 'POST'])
def get_session(request):
    if request.method == 'GET':
        session_id = request.COOKIES.get("sessionid")
        return JsonResponse({"SessionID": session_id})
