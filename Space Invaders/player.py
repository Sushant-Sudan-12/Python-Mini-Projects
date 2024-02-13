import turtle
from turtle import Turtle
import time
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.goto(0,-230)
        self.setheading(90)
        self.color("white")

    def move_r(self):
        if self.xcor()<250:
            self.teleport(self.xcor()+30,self.ycor())

    def move_l(self):
        if self.xcor()>-250:
            self.teleport(self.xcor()-30,self.ycor())

    def player_beam(self):
        beam = Turtle()
        beam.shape("circle")
        beam.teleport(self.xcor(),self.ycor())
        beam.color("blue")
        beam.shapesize(0.4)








