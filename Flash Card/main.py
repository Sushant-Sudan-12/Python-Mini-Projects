BACKGROUND_COLOR = "#B1DDC6"
WHITE_COLOR = "#FAEBD7"
Timer = None

from tkinter import *
import pandas as pd
import random

window = Tk()
window.title("Flash Card Game")
window.config(padx = 50,pady = 50)

canva = Canvas(width = 800, height = 526)
f_card = PhotoImage(file = "images/card_front.png")
e_card = PhotoImage(file = "images/card_back.png")
image = canva.create_image(400,263,image= f_card)
canva.grid(row = 0 , column=0,columnspan = 2)

data = pd.read_csv("data/french_words.csv")              # I COULD ALSO USE data.to_dict(orient = "records")
french = data.French.to_dict()
english = data.English.to_dict()

language = canva.create_text(400,150,text = "French",fill = BACKGROUND_COLOR,font = ("Arial",40,"italic") )
word = canva.create_text(400,263,text = french[random.randint(0,101)],fill = BACKGROUND_COLOR,font = ("Arial",60,"bold") )

def new_word1():

    n = random.randint(1, len(data.French.to_dict()))     # AFTER_CANCEL CAN BE USED TO OVERCOME THE PROBLEM
    lang = "French"                                          # OF CARDS SHOWING UP EVEN AFTER SKIPPING
    french_word = french[n]
    english_word = english[n]

    canva.itemconfig(image , image = f_card)
    canva.itemconfig(language,text = lang,fill = BACKGROUND_COLOR)
    canva.itemconfig(word,text = french_word,fill = BACKGROUND_COLOR)

    def solution():
        global Timer
        Timer = window.after(3000,sol)

    def sol():
        canva.itemconfig(image,image = e_card)
        canva.itemconfig(language,text = "English",fill = WHITE_COLOR)
        canva.itemconfig(word,text = english_word,fill = WHITE_COLOR)
    solution()

    del french[n]
    del english[n]
    print(len(french))
def new_word():

    n = random.randint(0, len(data.French.to_dict()))     # AFTER_CANCEL CAN BE USED TO OVERCOME THE PROBLEM
    lang = "French"                                          # OF CARDS SHOWING UP EVEN AFTER SKIPPING
    french_word = french[n]
    english_word = english[n]

    canva.itemconfig(image , image = f_card)
    canva.itemconfig(language,text = lang,fill = BACKGROUND_COLOR)
    canva.itemconfig(word,text = french_word,fill = BACKGROUND_COLOR)

    def solution():
        global Timer
        Timer = window.after(3000,sol)

    def sol():
        canva.itemconfig(image,image = e_card)
        canva.itemconfig(language,text = "English",fill = WHITE_COLOR)
        canva.itemconfig(word,text = english_word,fill = WHITE_COLOR)
    solution()


new_word()

tick = PhotoImage(file ="images/right.png")
right = Button(image =tick,highlightthickness=0,command = new_word1)
right.grid(row = 1, column = 0)

cross = PhotoImage(file = "images/wrong.png")
wrong = Button(image = cross,highlightthickness=0,command = new_word)
wrong.grid(row = 1 , column = 1)



window.mainloop()



