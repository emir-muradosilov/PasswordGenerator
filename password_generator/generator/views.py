from django.shortcuts import render

from django.http import HttpResponse
import random as r

def home(request):
    return render(request, 'generator/home.html', {'home':'This is my home!'})
# Create your views here.

def password(request):

    characters = [chr(i) for i in range(97,123)]
    chisla = [i for i in range(0,10)]
    specialsimvol = [chr(i) for i in range(33,48)]
    if request.GET.get('numbers') == 'on':
        characters += chisla
    if request.GET.get('specialsimvol') == 'on':
        characters += specialsimvol
    length = int(request.GET.get('length', 8))
    password = ''
    for i in range(length):
        var = r.choice(['l','a'])
        password += str(r.choice(characters)) if var == 'l' else str(r.choice(characters)).upper()

    return render(request, 'generator/password.html', {'password' : password })
# Create your views here.


def test(request):
    return HttpResponse('test - page')
