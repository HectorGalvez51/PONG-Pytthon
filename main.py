from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=1080, height=720)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle = Paddle()
ball = Ball()
score = Score()
screen.listen()
screen.onkey(paddle.up_right, 'Up')
screen.onkey(paddle.up_left, 'w')
screen.onkey(paddle.down_right, 'Down')
screen.onkey(paddle.down_left, 's')
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 340 or ball.ycor() < -320:
        ball.bounce_y()

    if ball.distance(paddle.right[0]) < 50 and ball.xcor() > 490:
        ball.bounce_x()
    elif ball.distance(paddle.left[0]) < 50 and ball.xcor() < -500:
        ball.bounce_x()

    if ball.xcor() > 520:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -520:
        ball.reset_position()
        score.r_point()
screen.exitonclick()
