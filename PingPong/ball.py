from turtle import Turtle
import random
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("DarkOrange3")
        self.shapesize(0.8)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move_ball(self):
        self.penup()
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def centre_spawn(self):
        self.move_speed = 0.1
        self.penup()
        self.goto(0,0)
        self.x_move*=-1

    def bounce(self):
        self.y_move *= -1

    def bounce_p(self):
        self.move_speed *=0.8
        self.x_move *=-1

