from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UserInterface:
    def __init__(self,quiz_Brain:QuizBrain):
        self.quiz = quiz_Brain

        self.window = Tk()
        self.window.minsize(300,300)
        self.window.config(padx = 50,pady=50)
        self.score = 0

        self.label1 = Label(text = f"Score:{self.score}",fg = 'white',bg = THEME_COLOR)
        self.label1.grid(row = 0,column = 1)

        self.canva = Canvas(width = 300,height = 250,bg = "white")
        self.current = self.canva.create_text(150,125,width = 280,text = "Some Question",fill = THEME_COLOR,font = ("Arial",20,"normal"))
        self.canva.grid(row = 1,column = 0,columnspan = 2)

        right = PhotoImage(file="images/true.png")
        self.right = Button(image=right,command = self.right)
        self.right.grid(row=2, column=0)

        wrong = PhotoImage(file="images/false.png")
        self.wrong = Button(image=wrong,command = self.wrong)
        self.wrong.grid(row=2, column=1)

        self.next_question_ui()

        self.window.mainloop()

    def next_question_ui(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canva.itemconfig(self.current,text = q_text)
        else:
            self.canva.itemconfig(self.current,text = f"You have reached th end your score is {self.score}/10.")
            self.right.config(state = "disabled")
            self.wrong.config(state = "disabled")


    def right(self):
        if(self.quiz.check_answer("true")):
            self.canva.config(bg="green")
            self.window.after(1000,self.turn_white)
            self.score+=1
            self.label1.config(text = f"Score:{self.score}")
        else:
            self.canva.config(bg="red")
            self.window.after(1000, self.turn_white)


    def wrong(self):
        if(self.quiz.check_answer("false")):
            self.canva.config(bg="green")
            self.window.after(1000, self.turn_white)
            self.score += 1
            self.label1.config(text=f"Score:{self.score}")

        else:
            self.canva.config(bg="red")
            self.window.after(1000, self.turn_white)



    def turn_white(self):
        self.canva.config(bg = "white")
        self.next_question_ui()





