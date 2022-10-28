from django.shortcuts import render
from django.http import HttpResponse

rooms = [
    {'id':1, 'name': 'Crazy people room'},
    {'id':2, 'name': 'Backend Developers'},
    {'id':3, 'name': 'Design Lovers'},
]
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
