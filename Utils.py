# import only system from os
from os import system, name


# define our clear function
def Screen_cleaner():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# define vars
SCORES_FILE_NAME_A = "Scores.txt"
BAD_RETURN_CODE_A = "666"
