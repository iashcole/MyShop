from django.shortcuts import render, redirect


def index(request):
    return render(request, 'products/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')