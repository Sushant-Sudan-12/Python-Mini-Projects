from turtle import Turtle
import random
from snake import Snake

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5,0.5)
        self.spawner()

    def spawner(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)


