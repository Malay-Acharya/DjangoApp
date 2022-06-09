from django.shortcuts import render
from django.http import HttpResponse

from discordapp.settings import ROOT_URLCONF

rooms = [
    {'id':1, 'name':"room1"},
    {'id':2, 'name':"room2"},
    {'id':3, 'name':"room3"},
]

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html', {'rooms': rooms})
