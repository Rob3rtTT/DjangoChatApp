from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request, 'chat/index.html', {'title': 'Choose Room'})
@login_required(login_url='/login/')
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def about(request):
    return render(request, 'chat/about.html', {'title': 'About'})