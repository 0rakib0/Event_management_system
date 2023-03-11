from django.shortcuts import render
from .models import Artist
# Create your views here.

def Home(request):
    artist = Artist.get_artist_list()
    context = {
        'artist':artist
    }
    
    return render(request, 'customar/home.html', context)
