#!/usr/bin/python
import abcdbank

def read_cards_typed():
    n = input("Enter quantity of credit cards numbers that you will type:")

    for i in range(0, int(n)):
        card_number = input("Enter your credit card number: ")
        card = abcdbank.CreditCard(card_number)
        print card.check_valid_card_number()

def read_cards_file(path):
    cards_file = open(path, "r")
    n = int(cards_file.read(1).strip())
    cards_file_len = sum(1 for line in cards_file)

    if 1 <= n <= 100 and n == cards_file_len-1:
        cards_file.seek(2)
        for line in cards_file:
            card = abcdbank.CreditCard(line.strip())
            print line.rstrip()+'-'+card.check_valid_number()
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