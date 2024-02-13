from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.score_card()

    def score_card(self):
        self.color("black")
        self.goto(100,250)
        self.write(f"Score:{self.r_score}", True, "center", ("Arial", 20, "normal"))
        self.color("red")
        self.goto(-100,250)
        self.write(f"Score:{self.l_score}", True, "center", ("Arial", 20, "normal"))


    def score_l(self):
        self.clear()
        self.l_score+=1
        self.score_card()

    def score_r(self):
        self.clear()
        self.r_score+=1
        self.score_card()

    def check_win(self):
        if self.l_score == 3 :
            self.goto(25,0)
            self.color("red")
            self.write("Red Wins", True, "center", ("Arial", 50, "normal"))
            return True
        if self.r_score == 3:
            self.goto(25, 0)
            self.color("black")
            self.write("Black Wins", True, "center", ("Arial", 50, "normal"))
            return True