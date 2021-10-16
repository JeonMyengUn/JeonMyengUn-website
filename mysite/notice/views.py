from django.shortcuts import render
from django.http import HttpResponse

from .models import board 

def notice(request):
    boards = board.objects
    return render(request, 'index.html', {'boards':boards})