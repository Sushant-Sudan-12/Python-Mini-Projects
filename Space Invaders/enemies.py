from turtle import Turtle

class Enemies:

    def __init__(self):
        self.enemy_list = []
        self.spawn_enemy()
        self.level = 10


    def spawn_enemy(self):
        for y in range(230,531,30):
            for x in range(-240,61,30):
                enemy = Turtle()
                enemy.shape("square")
                enemy.penup()
                enemy.color("yellow")
                enemy.goto(x,y)
                self.enemy_list.append(enemy)

    def  move_enemies_l(self):
        for i in self.enemy_list:
            i.setheading(0)
            i.forward(30)

    def  move_enemies_r(self):
        for i in self.enemy_list:
            i.setheading(180)
            i.forward(30)

    def  move_enemies_d(self):
        for i in self.enemy_list:
            i.setheading(270)
            i.forward(30)

