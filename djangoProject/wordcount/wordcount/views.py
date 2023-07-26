from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1 style='color:blue'>Welcome to my Home page</h1>")


def about(request):
    return HttpResponse("<h1 style='color:purple'>Welcome to my About page</h1>")


def contact(request):
    return HttpResponse("<h1 style='color:red'>Welcome to my Contact page</h1>")
