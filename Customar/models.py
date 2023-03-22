from django.db import models
from Accounts.models import CustomUser
# Create your models here.


class Artist(models.Model):
    name             = models.CharField(max_length=120)
    image            = models.ImageField(upload_to='artist_pic')
    date_of_birth    = models.DateField()
    music_type       = models.CharField(max_length=120)
    youtube_channel  = models.URLField()
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    @staticmethod
    def get_artist_list():
        return Artist.objects.all()
        


class Buyer_info(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ticket')
    Full_name = models.CharField(max_length=150)
    email = models.EmailField()
    price = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    num_of_ticket = models.IntegerField(default=1)
    aditional_request = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.email
    

  
    def ticket_number(self):
        return self.num_of_ticket
         


class Ticket(models.Model):
    normal_ticket_price  = models.IntegerField()
    premium_ticket_price = models.IntegerField()
    Total_seat           = models.IntegerField()
    # available_seat       = models.IntegerField(default=Total_seat, blank=True, null=True)
    created_at           = models.DateTimeField(auto_now_add=True)
    updated_at           = models.DateTimeField(auto_now=True)


    @staticmethod
    def get_ticket():
        return Ticket.objects.all()
         


 