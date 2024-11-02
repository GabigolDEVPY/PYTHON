import os 
import json
import random

def clear():
    os.system("cls")

Base_directory = os.path.dirname(os.path.abspath(__file__))

list_dict = os.path.join(Base_directory, "words.json")
list_scores_lifes = os.path.join(Base_directory, "data.json")

def load_list():
    try:
        with open(list_dict, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print('impossible to load the file')

def load_list_scores_lifes():
    try:
        with open(list_scores_lifes, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"scores": 0, "lifes": 0}

def save_file():
    with open(list_scores_lifes, "w") as f:
        json.dump(data, f)

list = load_list()
data = load_list_scores_lifes()




