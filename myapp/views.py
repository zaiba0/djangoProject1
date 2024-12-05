
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Assalamualikum zaiba</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')