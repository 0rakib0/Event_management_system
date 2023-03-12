from django.shortcuts import render
from .models import Artist, Ticket
# Create your views here.

def Home(request):
    artist = Artist.get_artist_list()
    t = Ticket.get_ticket()
    print(request.GET)
    context = {
        'artist':artist,
        't':t
    }
    
    return render(request, 'customar/home.html', context)


def Buy_ticket(request, price):
    print('-----------------')
    print(price)
    context = {

    }
    return render(request, 'customar/ticket.html', context)

