from turtle import Turtle

class Markings:

    def __init__(self):
        self.outer_markings()

    def outer_markings(self):
        mark = Turtle()
        mark.hideturtle()
        mark.color("white")
        mark.goto(0,295)
        mark.goto(445,295)
        mark.goto(445,-295)
        mark.goto(-445,-295)
        mark.goto(-445,295)
        mark.goto(0,295)
        mark.goto(0,-295)

