from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("orange")
        self.setheading(90)
        self.goto(0,-280)

    def move(self):
        self.forward(100)

