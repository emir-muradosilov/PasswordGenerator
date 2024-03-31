from django.shortcuts import render

from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html', {'home':'This is my home!'})
# Create your views here.

def password(request):
    return render(request, 'generator/password.html', {'password':generate_password()})
# Create your views here.

def generate_password():
    import random as r
    alphavit = [chr(i) for i in range(97,123)]
    chisla = [i for i in range(0,10)]
    res = alphavit + chisla
    rand=''
    for i in range(10):
        rand += str(r.choice(res))
    return rand

def test(request):
    return HttpResponse('test - page')
