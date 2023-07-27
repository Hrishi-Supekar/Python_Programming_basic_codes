from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'Home.html', {'name': 'Hrishi'})


def about(request):
    return render(request, 'about.html', {'age': 28, 'city': 'Pune'})


def contact(request):
    return render(request, 'contact.html', {'mobile': '+91 9658745214'})


def form(request):
    if request.method == "POST":
        a = int(request.POST.get("n1"))
        b = int(request.POST.get("n2"))
        ans = a + b
        return render(request, 'calculator.html', {'ans': ans})
    else:
        return render(request, 'calculator.html')
