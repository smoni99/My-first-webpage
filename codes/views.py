from django.http import HttpResponse
from django.shortcuts import render
from . models import Code


def index(request):
    codes = Code.objects.all()
    return render(request, 'index.html', {'codes': codes})


def Würfel(request):
    return render(request, 'Würfel.html')


def Hangman_allein(request):
    return render(request, 'Hangman_allein.html')


def Hangman_für_zwei(request):
    return render(request, 'Hangman_für_zwei.html')