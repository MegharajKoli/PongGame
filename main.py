from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()
screen.setup(height=700,width=800)
screen.bgcolor("black")
screen.tracer(0)
scoreboard=Scoreboard()

r_paddle=Paddle(350)
l_paddle=Paddle(-350)
ball=Ball()
screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

game_is_on=True
while (game_is_on):
    time.sleep(0.1)
    screen.update()
    ball.moving()

    #detect collision with wall
    if ball.ycor()>330 or ball.ycor()<-330:
        ball.y_bounce()

    #Collison with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>330 or ball.distance(l_paddle)<50 and ball.xcor()<-330:
        ball.x_bounce()

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score==5:
        scoreboard.l_winner()
        game_is_on=False

    if scoreboard.r_score==5:
        scoreboard.r_winner()
        game_is_on=False
screen.exitonclick()
