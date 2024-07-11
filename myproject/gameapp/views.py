from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint

# Create your views here.

def index(request):
    return HttpResponse("Hello")

def home_page(request):
    return render(request, 'marketapp/home_game.html')

def orel(request):
    return HttpResponse(choice(['Орел', 'Решка']))

def kubik(request):
    return HttpResponse(randint(1,6))