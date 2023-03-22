from django.shortcuts import render, redirect
from .models import Artist, Ticket, Buyer_info
from Accounts.models import CustomUser as User
from django.contrib.auth.decorators import login_required
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

@login_required
def Buy_ticket(request, price):
    price = price
    user = User.objects.get(id=request.user.id)
    ticket = Ticket.objects.all()
    for i in ticket:
        total_seat = i.Total_seat
    #     return total_seat
    # print(total_seat)
    print('-------------------------')
    if request.method == "POST":
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        ticket_price = request.POST.get('ticket_price')
        number_of_ticket = request.POST.get('num_tiket')
        ticket_message = request.POST.get('ticket_message')

        Buyer = Buyer_info(
            user = request.user,
            Full_name = full_name,
            email = email,
            price = ticket_price,
            num_of_ticket = number_of_ticket,
            aditional_request = ticket_message,
            phone_number = phone
        )
        if Buyer:
            # tickets = (total_seat - number_of_ticket)
            # ticket.Total_seat = tickets
            # ticket.save()
            # Buyer.save()
            return redirect('customar:home')

    context = {
        'price':price,
        'user':user
    }
    return render(request, 'customar/ticket.html', context)

