from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from django.views import generic


def index(request):
    return render(request, 'home/index.html')