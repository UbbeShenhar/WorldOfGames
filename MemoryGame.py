from random import choice
import collections
import time


def generate_sequence(difficulty):
    selection_list = []
    sequence = [i for i in range(1, 101)]
    for _ in range(difficulty):
        selection = choice(sequence)
        selection_list.append(selection)
    print(selection_list, end='')
    time.sleep(0.7)
    print("\r"" ")
    return selection_list


def get_list_from_user(difficulty):
    user_list = list(map(int, input(
        "\nEnter the list of numbers between 1 to " + str(difficulty) + " separated by space : ").strip().split()))
    if not 1 <= len(user_list) <= difficulty:
        print("Error: Too many numbers were entered!\n", "Please enter number between 1 to", difficulty)
        del user_list
    # print(user_list)
    return user_list


def is_list_equal(difficulty):
    selection_list = generate_sequence(difficulty)
    user_list = get_list_from_user(difficulty)
    if collections.Counter(user_list) == collections.Counter(selection_list):
        result = "True"
    else:
        result = "False"
    return result


def play(difficulty):
    result = is_list_equal(difficulty)
    print(result)
    return result
