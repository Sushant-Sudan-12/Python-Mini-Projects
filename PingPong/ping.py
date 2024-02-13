from turtle import Turtle

class Ping(Turtle):
    def __init__(self,x,y,color):
        super().__init__()
        self.create_handle(x,y,color)


    def create_handle(self,x,y,color):
        self.shape("square")
        self.color(color)
        self.shapesize(3,0.5)
        self.teleport(x,y)

    def move_up(self):
        self.penup()
        self.goto(self.xcor(),self.ycor()+40)

    def move_down(self):
        self.penup()
        self.goto(self.xcor(),self.ycor()-40)

















    # def __init__(self):
    #     self.create_ping(-420,0,"red")
    #     self.create_top(-420,30,"black")
    #     self.create_ping(420,0,"black")
    #     self.create_top(420,30,"red")
    #
    #
    # def create_ping(self,x,y,color):
    #     turtle1 = Turtle()
    #     turtle1.penup()
    #     turtle1.shape("square")
    #     turtle1.color(color)
    #     turtle1.shapesize(3,0.5)
    #     turtle1.teleport(x,y)
    #
