from django.shortcuts import render
from .models import *

def index(request):
    return render(request, 'index.html')

def photo(request, numb):
    data = MenuItem.objects.get(id=numb) 
    resp = {
        'photo': data,
    }
    return render(request, 'photo.html', resp)