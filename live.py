from GuessGame import play as GuessGamePlay
from MemoryGame import play as MemoryGamePlay
from CurrencyRouletteGame import play as CurrencyRouletteGamePlay
from Score import add_score


def welcome(name):
    output = print("Hello", name, "and welcome to the World of Games (WoG).\n" "Here you can find many cool games to play.")
    return output


def load_game():
    global difficulty, result
    choose = int(input('Please choose a game to play: \n'
                       '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n'
                       '2. Guess Game - guess a number and see if you chose like the computer\n'
                       '3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n'))
    if 1 <= choose <= 3:
        if choose == 1:
            difficulty = int(input("Please choose game difficulty from 1 to what you want: "))
            result = GuessGamePlay(difficulty)
        elif choose == 2:
            difficulty = int(input("Please choose game difficulty from 1 to what you want: "))
            result = MemoryGamePlay(difficulty)
        elif choose == 3:
            difficulty = int(input("Please choose game difficulty from 1 to 5: "))
            result = CurrencyRouletteGamePlay(difficulty)

        if result == "True":
            print("You won!")
            add_score(difficulty)

    else:
        print('Error: Please enter number between 1-3')
