from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'Home.html', {'name': 'Hrishi'})


def about(request):
    return render(request, 'about.html', {'age': 28, 'city': 'Pune'})


def contact(request):
    return render(request, 'contact.html', {'mobile': '+91 9658745214'})


def form(request):
    return render(request, 'calculator.html')
