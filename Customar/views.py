from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Artist, Ticket, Buyer_info, Wallet
from Accounts.models import CustomUser as User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import Http404
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
    wallete = Wallet.objects.filter(user=request.user.id)
    for i in wallete:
        ballance = i.wallet_ballance
    for i in ticket:
        total_seat = i.Total_seat
        
    if request.method == "POST":
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        ticket_price = request.POST.get('ticket_price')
        number_of_ticket = request.POST.get('num_tiket')
        ticket_message = request.POST.get('ticket_message')
        
        ticket_price = int(ticket_price) * int(number_of_ticket)
        if Buyer_info.objects.filter(email=email).first():
            messages.warning(request, 'You have already booked ticket!')
            return HttpResponseRedirect(reverse('customar:ticket', args=[price]))
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
            ballances = int(ballance) - int(ticket_price)
            if ballances <= 0:
                messages.warning(request, 'Blance is not enough. You have only '+ str(ballance)+' tk')
                return HttpResponseRedirect(reverse('customar:ticket', args=[price]))
            for i in wallete:
                i.wallet_ballance = ballances
                i.save()
            tickets = int(total_seat) - int(number_of_ticket)
            if tickets <= 0:
                messages.warning(request, 'ticket is not enough. only '+str(total_seat)+' seats available')
                return HttpResponseRedirect(reverse('customar:ticket', args=[price]))
            up_ticket = Ticket.objects.all()
            for i in up_ticket:
                i.Total_seat = tickets
                i.save()
            Buyer.save()
            messages.success(request, 'Ticket sucessfully booked!')
            return HttpResponseRedirect(reverse('customar:ticket', args=[price]))

    context = {
        'price':price,
        'user':user
    }
    return render(request, 'customar/ticket.html', context)

def Add_balace(request):
    user = request.user
    wallet = Wallet.objects.get_or_create(user=user)
    wallets = Wallet.objects.get(user=user)
    
    present_balance = wallets.wallet_ballance
    if request.method == "POST":
        blance = request.POST.get('balance')    
        blance = float(present_balance) + float(blance)
        wallet = Wallet.objects.get(user=user)
        wallet.wallet_ballance = blance
        wallet.save()
        return redirect('Login:profile') 
    return Http404("Something went wrong!")

