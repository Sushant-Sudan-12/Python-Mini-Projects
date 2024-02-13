from turtle import Turtle

pos = [(0,0),(-20,0),(-40,0)]
class Snake():

    def __init__(self):

        self.segment = []
        self.create_snake()
        self.head = self.segment[0]


    def create_snake(self):
        for i in pos:
            self.add_segment(i)

    def add_segment(self,positon):
        turtle = Turtle()
        turtle.penup()
        turtle.goto(positon)
        turtle.shape("square")
        turtle.color("white")
        self.segment.append(turtle)

    def snake_reset(self):
        for i in self.segment:
            i.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def eaten(self):
        self.add_segment(self.segment[-1].pos())

    # def eaten(self):
    #     turtle = Turtle()
    #     turtle.hideturtle()
    #     turtle.penup()
    #     turtle.shape("square")
    #     self.segment.append(turtle)
    #     turtle.color("white")
    #     turtle.showturtle()



    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            self.segment[i].goto(self.segment[i-1].pos())
        self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading()!=270:
            self.segment[0].setheading(90)

    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)


