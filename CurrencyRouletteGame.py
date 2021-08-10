from currency_converter import CurrencyConverter
from random import randint


def generate_number():
    number = randint(1, 100)
    return number


def currency_converter():
    number = generate_number()
    c = CurrencyConverter()
    # single_currency = c.convert(1, 'USD', 'ILS')
    currency = c.convert(number, 'USD', 'ILS')
    return currency


def get_money_interval(difficulty):
    currency = currency_converter()
    d = difficulty
    t = currency
    interval = (t - (5 - d), t + (5 - d))
    return interval


def get_guess_from_user():
    number = generate_number()
    print("The generate number is - ", number)
    guess = float(input("Please guess the value of the generated number from USD to ILS: "))
    return guess


def check_result(difficulty):
    interval = get_money_interval(difficulty)
    guess = get_guess_from_user()
    if interval[0] <= guess <= interval[1]:
        result = "True"
    else:
        result = "False"
    return result


def play(difficulty):
    result = check_result(difficulty)
    print(result)
    return result
