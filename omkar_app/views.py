from django.shortcuts import render, redirect

from django.conf import settings


def home(request):
    return render(request,'home.html')

