import os
import uuid
import shutil
from collections import OrderedDict
from pyramid.view import view_config
import card_validator.abcdbank as bank

"""Common Views

Class containing common views 
"""
class CommonViews:
    def __init__(self, request):
        self.request = request

    """Return an empty dict

    View to 404 page
    """
    @view_config(context='pyramid.httpexceptions.HTTPNotFound', 
                 renderer='404.jinja2')
    def not_found(self):
        return {}

"""Card Validator Views

Class containing all the views related to credit card numbar validator
"""
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
        cards_validated = OrderedDict()
        message = ''
        if 'validate-typed' in self.request.params:
            n = int(self.request.params['cards-count'])
            if self.request.params['cards-list'] != "":
                cards = self.request.params['cards-list'].split("\n")
                if n == len(cards):
                    for card_number in cards:
                        card = bank.CreditCard(card_number.strip())
                        cards_validated[card_number] = card.check_valid_number()
                else:
                    message = ("The quantity of card's numbers typed " \
                               "must correspond to the given quantity.\n" \
                               "(You typed {0} number instead of {1})"
                               .format(len(cards), n))
            else:
                message = "The list of card's numbers can not be empty."

        return dict(cards_validated=cards_validated, message=message)

    """Return a dict

    Verify and returns card numbers in a file and if they're valid or not
    """
    @view_config(route_name='validator_file', 
                renderer='cards_validated.jinja2')
    def cards_file_validator(self):
        cards_validated = OrderedDict()
        message = ''
        if 'upload-file' in self.request.params:

            # Upload the file containing card numbers
            # Create a new name to prevent insecure paths on filename 
            filename = self.request.POST['cards-file'].filename
            input_file = self.request.POST['cards-file'].file
            file_path = os.path.join(
                                'card_validator/files', 
                                '%s.txt' % uuid.uuid4()
                                )
            temp_file_path = file_path + '~'
            input_file.seek(0)
 
            with open(temp_file_path, 'wb') as output_file:
                shutil.copyfileobj(input_file, output_file)

            os.rename(temp_file_path, file_path)

            # Read the file and validate card numbers
            cards_file = open(file_path, "r")
            n = int(cards_file.read(1).strip())
            cards_file_len = sum(1 for line in cards_file)

            if 1 <= n <= 100 and n == cards_file_len-1:
                cards_file.seek(2)
                for card_number in cards_file:
                    card = bank.CreditCard(card_number.strip())
                    cards_validated[card_number] = card.check_valid_number()
            else:
                message = ("The first line in the file must contain the " \
                           "correct quantity of card's numbers and the " \
                           "number must be between 1 and 100")
            cards_file.close()

        return dict(cards_validated=cards_validated, message=message)
