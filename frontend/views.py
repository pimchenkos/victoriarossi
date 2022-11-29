from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    return render(request, 'frontend/main.html')


def index(request):
    return render(request, 'frontend/index.html')


def services(request):
    return render(request, 'frontend/services.html')


def aboutMe(request):
    return render(request, 'frontend/aboutMe.html')


def contacts(request):
    return render(request, 'frontend/contacts.html')


def clients(request):
    if request.user.is_staff:
        return render(request, 'frontend/clients.html')
    else:
        return HttpResponse('Страница недоступна')
