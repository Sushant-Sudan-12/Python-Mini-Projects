import time
from turtle import Turtle , Screen
from ping import Ping
from ball import Ball
from table_markings import Markings
import time
from score import Score

screen = Screen()
screen.bgcolor("CornflowerBlue")
screen.setup(900,600)
screen.tracer(0)

marking = Markings()
ping1 = Ping(430,0,"black")
ping2 = Ping(-430,0,"red")
ball = Ball()
score = Score()

screen.listen()
screen.onkey(ping1.move_up,"Up")
screen.onkey(ping2.move_up,"w")
screen.onkey(ping1.move_down,"Down")
screen.onkey(ping2.move_down,"s")
score.score_card()

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)


    ball.move_ball()
    if score.check_win():
        is_game_on = False

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if ball.xcor()>410 and ball.distance(ping1)<60:
        ball.bounce_p()

    if ball.xcor()<-410 and ball.distance(ping2)<60:
        ball.bounce_p()

    if ball.xcor()>460:
        score.score_l()
        time.sleep(1)
        ball.centre_spawn()

    if ball.xcor()<-460:
        score.score_r()
        time.sleep(1)
        ball.centre_spawn()







screen.exitonclick()