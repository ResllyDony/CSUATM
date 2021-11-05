# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def Hello_World(Request):
    return render(Request, 'hello.html')