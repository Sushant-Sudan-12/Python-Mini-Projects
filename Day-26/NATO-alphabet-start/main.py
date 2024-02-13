import pandas

list = pandas.read_csv("nato_phonetic_alphabet.csv")
list.to_dict()

#TODO 1. Create a dictionary in this format:

phonetic_dict = {row.letter:row.code for (index,row) in list.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter the name: ")
name = name.upper()
list = [ n for n  in name]

dict = {letter:code for (letter,code) in phonetic_dict.items() if letter in list}
print(dict)

dict1 = [phonetic_dict[letter] for letter in list]
print(dict1)