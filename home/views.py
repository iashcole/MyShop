from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.views import generic


def index(request):
    return render(request, 'products/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')