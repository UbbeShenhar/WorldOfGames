from random import randint


def generate_number(difficulty):
    secret_number = randint(1, difficulty)
    return secret_number
    # print(secret_number)


def get_guess_from_user(difficulty):
    guess = int(input("Please guess a number between 1 to " + str(difficulty) + ": "))
    return guess
    # print(guess)


def compare_results(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    if secret_number == guess:
        result = "True"
    else:
        result = "False"
    return result


def play(difficulty):
    result = compare_results(difficulty)
    print(result)
    return result
