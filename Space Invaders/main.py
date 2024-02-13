import time
from turtle import Turtle,Screen
import player
import enemies

screen = Screen()
screen.bgcolor("black")
screen.setup(600,500)
screen.tracer(0)

player1 = player.Player()
enemy1 = enemies.Enemies()

screen.listen()
screen.onkey(player1.move_r,"Right")
screen.onkey(player1.move_l,"Left")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    player1.player_beam()

    for _ in range(6):
        screen.update()
        time.sleep(0.5)
        enemy1.move_enemies_l()



    for _ in range(1):
        screen.update()
        time.sleep(0.5)
        enemy1.move_enemies_d()


    for _ in range(6):
        screen.update()
        time.sleep(0.5)
        enemy1.move_enemies_r()


    for _ in range(1):
        screen.update()
        time.sleep(0.5)
        enemy1.move_enemies_d()

    for i in enemy1.enemy_list:
        if i.ycor() < -200 :
            is_game_on = False



screen.exitonclick()