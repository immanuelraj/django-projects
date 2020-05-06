import sys
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from hotel.models import Room
from pyfiglet import Figlet

f = Figlet(font='slant')

style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})

class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Please enter a number',
                cursor_position=len(document.text))  # Move cursor to end

questions = [
    {
        'type': 'input',
        'name': 'budget',
        'message': 'Provide your budget in USD to get rooms',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    }
]

def main():
    print (f.renderText('Hi, welcome to United Layer'))
    print ('Kindly provide a below details to view the rooms')
    answers = prompt(questions, style=style)
    rooms = Room.objects.filter(total_room_price__lte=answers['budget'])
    for room in rooms:
        print('The Room Name {0}\n The room type {1} \n Max Occupancy {3}\n The Wifi price {4} \n \
            The Breakfast price {5}\n The A/C price {6} \n The Couch price {7}\n The Table price {8} \n  \
            The TV price {9}\n The Room price {10} \n The Total price {11}\n'.format(room.display_name, room.room_type,\
            room.max_occupancy, room.wifi_price, room.bearkfast_price, room.ac_price, room.couch_price, room.table_price,\
            room.tv_price, room.room_price, room.total_room_price))

if __name__ == '__main__':
    main()