import os
import uuid
import shutil
from pyramid.view import view_config
import card_validator.abcdbank as bank


class CardValidatorViews:
    def __init__(self, request):
        self.request = request

    """Return an empty dict

    Return an empty dictionary because there's nothing to be filled
    in template
    """
    @view_config(route_name='home', renderer='card_validator.jinja2')
    def home(self):
        return {}

    """Return a dict

    Verify and returns card numbers typed and if they're valid or not
    """
    @view_config(route_name='validator_typed', 
                renderer='cards_validated.jinja2')
    def cards_typed_validator(self):
        cards_validated = {}
        if 'validate-typed' in self.request.params:
            cards = self.request.params['cards-list'].split("\n")
            for card_number in cards:
                card = bank.CreditCard(card_number.strip())
                cards_validated[card_number] = card.check_valid_number()
        return dict(cards_validated=cards_validated)

    """Return a dict

    Verify and returns card numbers in a file and if they're valid or not
    """
    def cards_file_validator(self):
        if 'submit' in self.request.params:
            if 'cards-file' in self.request.params:
                cards_file = open(path, "r")
                n = int(cards_file.read(1).strip())
                cards_file_len = sum(1 for line in cards_file)

                if 1 <= n <= 100 and n == cards_file_len-1:
                    cards_file.seek(2)
                    for line in cards_file:
                        card = abcdbank.CreditCard(line.strip())
                        str_ = line.rstrip()+'-'+card.check_valid_number()
                cards_file.close()

                return {str_}
        return {}
