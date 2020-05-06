from django.contrib import admin
from hotel.models import Hotel, Room


class HotelAdmin(admin.ModelAdmin):
    exclude = ('ext_id',)
    search_fields = ('id','ext_id', 'name')
    list_display = [
        'id',
        'name',
        'address',
        'property_type',
        'contact_person',
    ]

class RoomAdmin(admin.ModelAdmin):
    exclude = ('ext_id', 'total_room_price')
    search_fields = ('id','ext_id',)
    list_filter = ('hotel__name',)
    list_display = [
        'id',
        'room_type',
        'display_name',
        'max_occupancy',
        'room_price',
        'total_room_price',
    ]

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)