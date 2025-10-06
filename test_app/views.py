from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>hello habr!!!<h1>") # вывод на нашу HTML страницу.
