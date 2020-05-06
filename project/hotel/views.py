from django.shortcuts import render, Http404
from hotel.models import Hotel, Room

def room_list_view(request):
    rooms = Room.objects.all()
    if request.GET.get('budget'):
        rooms = rooms.filter(total_room_price__lte=request.GET.get('budget'))
    return render(request, 'roomList.html', context={'data': rooms})