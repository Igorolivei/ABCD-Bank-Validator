#!/usr/bin/python
import abcdbank as bank

"""Read N cards and return if they are valid or not
"""
def read_cards_typed():
    n = input("Enter quantity of credit cards numbers that you will type:")

    if 1 <= n <= 100:
        for i in range(0, int(n)):
            card_number = input("Enter your credit card number: ")
            card = bank.CreditCard(card_number)
            print card.check_valid_number()
    else:
        print ("The quantity of credit card numbers must be between 1 and 100")

"""Read a file containing N cards and return if they are valid or not
"""
def read_cards_file(path):
    cards_file = open(path, "r")
    n = int(cards_file.read(1).strip())
    cards_file_len = sum(1 for line in cards_file)

    if 1 <= n <= 100 and n == cards_file_len-1:
        cards_file.seek(2)
        for line in cards_file:
            card = bank.CreditCard(line.strip())
            print line.rstrip()+'-'+card.check_valid_number()
    else:
        print ("The first line in the file must contain the " \
                           "correct quantity of card's numbers and the " \
                           "number must be between 1 and 100")
    cards_file.close()

if __name__ == "__main__":
    user_input = input("Choose your option:\nR - Read a file\nT - Type credit cards numbers\n")

    if str(user_input) == 'R':
        file_path = input("Enter the path of your file: ")
        read_cards_file(file_path)
    elif user_input == 'T':
        read_cards_typed()
    else:
        print "Invalid Option"
