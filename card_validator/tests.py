import unittest

from pyramid import testing
from card_validator.models import abcdbank as bank

class FunctionalTests(unittest.TestCase):

    def test_card_valid(self):
        card_number = '4321-1234-5678-4321'
        card = bank.CreditCard(card_number)
        self.assertEqual(card.check_valid_number(), 'Valid')

    def test_card_invalid(self):
        card_number = '5642-2221-1234-3212'
        card = bank.CreditCard(card_number)
        self.assertEqual(card.check_valid_number(), 'Invalid')