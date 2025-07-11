
from tkinter.font import names

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

nato_phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetic)

names_dic = {row.letter:row.code for (index,row) in nato_phonetic.iterrows()}

def generate_phonetic():

    user_input = input("Enter a word : ").upper()
    try:
        # output_list = [let + "-" + names_dic[let] for let in user_input]
        output_list = [names_dic[letter] for letter in user_input]
    except KeyError:
        print("Sorry. Only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()