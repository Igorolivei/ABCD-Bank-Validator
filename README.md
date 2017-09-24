ABCD Bank - Credit Card Validator
==========
ABCD Bank - Credit Card Validator is a little project made with Python, Pyramid web framework and Jinja2.
Is used to validate if a credit card is a valid ABCD Bank's credit card or not.

A valid ABCD Bank's credit card has the following characteristics:
* It must start with a 4, 5 or 6. 
* It must contain exactly 16 digits. 
* It must only consist of digits (0-9). 
* It may have digits in groups of 4, separated by one hyphen "-". 
* It must NOT use any other separator like ' ' , '_', etc. 
* It must NOT have 4 or more consecutive repeated digits.

Dependencies
------------
- Python 3
- Pyramid 1.9.1

Installing and Running (on Linux)
---------------------------------

- Set an environment variable:
:: $ export VENV=~/my_path/env
- Create a virtual environment:
:: $ python3 -m venv $VENV
- Clone this repository:
:: $ git clone https://github.com/Igorolivei/ABCD-Bank-Validator.git
- Run setup.py:
:: $ $VENV/bin/pip install -e .
- Initialize PyContacts using development.ini:
In development:
:: $ $VENV/bin/pserve development.ini --reload
In production:
:: $ $VENV/bin/pserve production.ini --reload

- If you want to execute on terminal:
:: $ cd card_validator; ./app.py
