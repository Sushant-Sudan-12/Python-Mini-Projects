from turtle import Turtle

class Background(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.color("blue")
        self.hideturtle()


    def lines(self):
        self.pendown()
        self.teleport(-400, -250)
        self.forward(800)
        self.teleport(-400, 250)
        self.forward(800)

    def score(self):
        self.penup()
        self.teleport(-350, 270)
        self.write(f"Level : {self.level}", True, "center", ("Arial", 15, "normal"))

    def next_level(self):
        self.clear()
        self.penup()
        self.level+=1
        self.teleport(-350, 270)
        self.write(f"Level : {self.level}", True, "center", ("Arial", 15, "normal"))

    def game_over(self):
        self.penup()
        self.color("black")
        self.goto(0,0)
        self.write("GAME OVER",True,"center",("Arial",50,"normal"))
