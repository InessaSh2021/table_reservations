from django.contrib import admin
from .models import Table, Reservations

class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'seats', 'location')
    search_fields = ('name',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'table_id', 'reservation_time', 'duration_minutes')
    search_fields = ('customer_name',)
    list_filter = ('table_id',)


