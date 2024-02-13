with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    final_letter = letter.read()
    for name in names_list:
        stripped_name = name.strip()
        completed_letter = final_letter.replace("[name]",stripped_name)
        print(completed_letter)
        with open(f"./Output/ReadyToSend/LetterTo{stripped_name}.txt",mode = "w") as final:
            final.write(completed_letter)
            




