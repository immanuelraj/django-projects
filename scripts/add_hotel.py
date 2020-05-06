from __future__ import absolute_import, print_function, unicode_literals
import sys
import regex
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError
from hotel.models import Hotel
from pyfiglet import Figlet

f = Figlet(font='slant')


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


class PhoneNumberValidator(Validator):
    def validate(self, document):
        ok = regex.match('^([01]{1})?[-.\s]?\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})\s?((?:#|ext\.?\s?|x\.?\s?){1}(?:\d+)?)?$', document.text)
        if not ok:
            raise ValidationError(
                message='Please enter a valid phone number',
                cursor_position=len(document.text))  # Move cursor to end

print (f.renderText('Hi, welcome to United Layer \n Kindly provide a below details to create Hotel'))

questions = [
    {
        'type': 'input',
        'name': 'name',
        'message': 'Name of the property',
    },
    {
        'type': 'input',
        'name': 'address',
        'message': 'Address of the property',
    },
    {
        'type': 'input',
        'name': 'city',
        'message': 'Property located city name',
    },
    {
        'type': 'input',
        'name': 'country',
        'message': 'Property located country name',
    },
    {
        'type': 'input',
        'name': 'contact_name',
        'message': 'Contact person name',
    },
    {
        'type': 'input',
        'name': 'cantact_phone',
        'message': 'Cantact phone number',
        'validate': PhoneNumberValidator
    },
    {
        'type': 'list',
        'name': 'hotel_type',
        'message': 'Hotel type?',
        'choices': ['Apartment', 'Hotel', 'ApartHotel'],
        'filter': lambda val: val.lower()
    }
]

def main():
    answers = prompt(questions, style=style)
    hotel = Hotel.object.create(name = answers['name'], address = answers['address'], city = answers['city'], country = answers['country'],
        contact_name = answers['contact_name'], cantact_phone = answers['cantact_phone'], hotel_type = answers['hotel_type'])

    print (f.renderText('Hotel is sucessfully created. \n To add a room in this hotel, Use Hotel ID: ' + hotel.id))


if __name__ == '__main__':
    main()