from booking.models import Room
from pyfiglet import Figlet

f = Figlet(font='slant')

rooms = Room.objects.all()

def main():
    print (f.renderText('Hi, welcome to United Layer'))
    print ('View the list of rooms')
    for room in rooms:
        print('The Room Name {0}\n The room type {1} \n Max Occupancy {3}\n The Wifi price {4} \n \
            The Breakfast price {5}\n The A/C price {6} \n The Couch price {7}\n The Table price {8} \n  \
            The TV price {9}\n The Room price {10} \n The Total price {11}\n'.format(room.display_name, room.room_type,\
            room.max_occupancy, room.wifi_price, room.bearkfast_price, room.ac_price, room.couch_price, room.table_price,\
            room.tv_price, room.room_price, room.total_room_price))

if __name__ == '__main__':
    main()