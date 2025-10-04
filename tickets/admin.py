from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('origin','destination','depart_date','price','airline')
    list_filter = ('origin','destination','airline')
