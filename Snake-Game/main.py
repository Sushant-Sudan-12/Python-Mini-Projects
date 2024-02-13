import time
from turtle import Turtle,Screen
from snake import Snake
import food
import score

screen = Screen()

screen.setup(600,600)
screen.bgcolor("black")
screen.tracer(0)

snake1 = Snake()
is_game_on = True
food1 = food.Food()
score1 = score.Score()

while is_game_on:
    screen.update()
    time.sleep(0.08)
    snake1.move()

    if snake1.head.distance(food1)<18:
        food1.spawner()
        score1.print_score()
        snake1.eaten()

    for i in range(len(snake1.segment)-1,0,-1):
        if snake1.head.distance(snake1.segment[i])<15:
            score1.reset()
            snake1.snake_reset()
            break



    if snake1.head.xcor()> 300:
        snake1.head.teleport(-300)

    if snake1.head.xcor()< -300:
        snake1.head.teleport(300)

    if snake1.head.ycor()> 300:
        snake1.head.teleport(y=-300)

    if snake1.head.ycor()< -300:
        snake1.head.teleport(y=300)

    screen.listen()
    screen.onkey(snake1.up,"Up")
    screen.onkey(snake1.down,"Down")
    screen.onkey(snake1.right,"Right")
    screen.onkey(snake1.left,"Left")

screen.exitonclick()


