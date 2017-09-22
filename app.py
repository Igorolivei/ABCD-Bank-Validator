#!/usr/bin/python
import re

def check_valid_card_number(candidate):
    pattern = r'((?!.*(\d)\2{3,})[4,5,6](\d{15}))$'
    card_number = candidate.replace("-", "")
    if re.match(pattern, str(card_number)):
        return True
    return False

def read_card_number():
    card_number = input("Enter your credit card number: ")

    if check_valid_card_number(card_number):
        print "It's valid!"
    else:
        print "Sorry, the given credit card number is not valid."

read_card_number()
