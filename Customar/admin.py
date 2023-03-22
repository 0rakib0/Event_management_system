from django.contrib import admin
from .models import Artist, Ticket, Buyer_info
# Register your models here.


admin.site.register(Artist)
admin.site.register(Ticket)
admin.site.register(Buyer_info)