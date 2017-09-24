# ABCD Bank module
"""ABCD Bank module

Used to implement CreditCard class
Must be used to implement some other features (e.g.: client, accounts)
"""
import re

class CreditCard:
    def __init__(self, number):
        self.number = number

    """Return a string

    Verifies if a given credit card number is valid or invalid
    """
    def check_valid_number(self):
        #To validate format, quantity of digits, start digit, and separators
        pattern_format = ('(([4,5,6]\d{3}[-]\d{4}[-]\d{4}[-]\d{4})|'
                          '([4,5,6](\d{15})))$')
        #To detect consecutive repeated digits, even that are separated by hyphen
        pattern_repeated = (r'(((\d)\3{3,})|((\d)[-]\5{3,})|((\d)\7{1}[-]\7{2,})'
                            r'|((\d)\9{2}[-]\9{1,}))')

        if re.match(pattern_format, self.number) and \
           not re.search(pattern_repeated, self.number):
            return 'Valid'

        return 'Invalid'
