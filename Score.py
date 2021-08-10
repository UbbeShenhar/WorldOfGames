from Utils import *
from os import path


def calculate_score(difficulty):
    point_of_winning = int((difficulty * 3) + 5)
    scores_file = open(SCORES_FILE_NAME_A, "r")
    current_score = int(float(scores_file.readline()))
    scores_file.close()
    new_score = current_score + point_of_winning
    # print(new_score)
    return new_score


def add_score(difficulty):
    if path.exists(SCORES_FILE_NAME_A):
        # print("exist")
        new_score = calculate_score(difficulty)
        scores_file = open(SCORES_FILE_NAME_A, "w")
        scores_file.write(str(new_score))
    else:
        # print("not")
        scores_file = open(SCORES_FILE_NAME_A, "w+")
        scores_file.write("0")
    scores_file.close()
    # scores_file = open(SCORES_FILE_NAME_A, "r")
    # score = scores_file.readline()
    # scores_file.close()
    # print(score)
