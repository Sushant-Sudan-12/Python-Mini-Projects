from turtle import Turtle
import random

COLOR = ["red","blue","yellow","green"]


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.segment=[]
        self.speed = 20
        self.car_segment()

    def car_segment(self):
        for i in range(4):
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.setheading(180)
            self.segment.append(turtle)

    def spawn_cars(self):
        self.penup()
        color =random.choice(COLOR)
        for i in self.segment:
            i.goto(random.randint(600,3000), random.randint(-230, 230))
            i.color(color)



    def move_cars(self):
        self.segment[0].forward(self.speed)
        for i in range(3,0,-1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x,new_y)



