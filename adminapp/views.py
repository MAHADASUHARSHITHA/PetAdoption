from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h1 align=center>WELCOME TO ADMIN APP</h1>")