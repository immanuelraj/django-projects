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

print (f.renderText('Hi, welcome to United Layer \n Kindly provide a below details to create room'))

questions = [
    {
        'type': 'rawlist',
        'name': 'room_type',
        'message': 'Room type',
        'choices': ['1 BR', '2 BR', '3 BR', 'Studio']
    },
    {
        'type': 'input',
        'name': 'display_name',
        'message': 'Room Display Name',
    },
    {
        'type': 'input',
        'name': 'hotel_id',
        'message': 'Hotel ID for the room to be added?',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'max_occupancy',
        'message': 'Maximum No of occupancy?',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'room_price',
        'message': 'Provide room charges in USD',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'confirm',
        'name': 'wifi',
        'message': 'Is wifi availabe?',
        'default': True
    },
    {
        'type': 'input',
        'name': 'wifi_price',
        'message': 'Provide Wifi charges in USD',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'default': 0,
        'when': lambda answers: answers['wifi'] != False
    },
    {
        'type': 'confirm',
        'name': 'bearkfast',
        'message': 'Is Bearkfast availabe?',
        'default': True
    },
    {
        'type': 'input',
        'name': 'bearkfast_price',
        'message': 'Provide bearkfast charges in USD',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'default': 0,
        'when': lambda answers: answers['bearkfast'] != False
    },
    {
        'type': 'confirm',
        'name': 'tv',
        'message': 'Is TV availabe?',
        'default': True
    },
    {
        'type': 'input',
        'name': 'tv_price',
        'message': 'Provide TV charges in USD',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'default': 0,
        'when': lambda answers: answers['tv'] != False
    },
    {
        'type': 'confirm',
        'name': 'couch',
        'message': 'Is Extra Couch availabe?',
        'default': True,
    },
    {
        'type': 'input',
        'name': 'couch_price',
        'message': 'Provide Couch charges in USD',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'default': 0,
        'when': lambda answers: answers['couch'] != False
    },
    {
        'type': 'confirm',
        'name': 'table',
        'message': 'Is dinning table availabe?',
        'default': True
    },
    {
        'type': 'input',
        'name': 'table_price',
        'message': 'Provide dinning table charges in USD',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'default': 0,
        'when': lambda answers: answers['table'] != False
    },
    {
        'type': 'confirm',
        'name': 'ac',
        'message': 'Is A/C availabe?',
        'default': True
    },
    {
        'type': 'input',
        'name': 'ac_price',
        'message': 'Provide A/C charges in USD',
        'validate': NumberValidator,
        'filter': lambda val: int(val),
        'default': 0,
        'when': lambda answers: answers['ac'] != False
    },
]

def main():
    answers = prompt(questions, style=style)
    Room.object.create(room_type = answers['room_type'], room_display_name = answers['aroom_display_namec'], hotel_id = answers['hotel_id'],
            max_occupancy = answers['max_occupancy'], room_price = answers['room_price'], wifi_price= answers['wifi_price'],
            bearkfast_price = answers['bearkfast_price'], tv_price = answers['tv_price'], couch_price = answers['couch_price'],
            table_price = answers['table_price'], ac_price = answers['ac_price'])
    print (f.renderText('Room is sucessfully added'))
if __name__ == '__main__':
    main()