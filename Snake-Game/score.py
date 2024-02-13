from turtle import Turtle
import food
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score=(file.read())
        self.write(f"Score ={self.score} High Score = {self.high_score}",True,"center",("Arial",20,"normal"))

    def print_score(self):
        self.clear()
        self.goto(0,260)
        self.score+=1
        self.write(f"Score ={self.score} High Score = {self.high_score}", True, "center", ("Arial", 20, "normal"))


    def reset (self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("high_score.txt",mode = "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.goto(0,260)
        self.write(f"Score ={self.score} High Score = {self.high_score}",True,"center",("Arial",20,"normal"))

    def game_over(self):
        self.home()
        self.write("Game Over", True, "center", ("Arial", 30, "normal"))