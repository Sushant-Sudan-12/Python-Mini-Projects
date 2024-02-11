from turtle import Turtle,Screen
from player import Player
from background import Background
from cars import Cars
import time

screen = Screen()
screen.setup(800,600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
background = Background()

car_list = []
for _ in range(60):
    cars = Cars()
    cars.spawn_cars()
    car_list.append(cars)

screen.listen()
screen.onkey(player.move,"Up")

speed_x = 0.1
is_game_on = True
while is_game_on:
    time.sleep(speed_x)
    screen.update()

    background.score()
    background.lines()

    for i in car_list:
        i.move_cars()
        if i.segment[0].xcor()<-600:
            i.segment[0].teleport(1800,i.segment[0].ycor())
        if i.segment[0].distance(player)<8:
            background.game_over()
            is_game_on=False

    if player.ycor()>280:
        background.next_level()
        player.goto(0 , -280)
        background.lines()
        speed_x*=0.5



screen.exitonclick()



