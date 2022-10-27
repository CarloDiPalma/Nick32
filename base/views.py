from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id':1, 'name': 'Crazy people room'},
    {'id':2, 'name': 'Backend Developers'},
    {'id':3, 'name': 'Design Lovers'},
]
def home(request):
    return render(request, 'home.html', {'rooms': rooms})

def room(request):
    return render(request, 'room.html')
