from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Bong Game")
screen.bgcolor("black")


screen.tracer(0)
l_paddle = Paddle(x_cor=-350)
r_paddle = Paddle(x_cor=350)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_paddle_up, "Up")
screen.onkey(r_paddle.move_paddle_down, "Down")
screen.onkey(l_paddle.move_paddle_up, "w")
screen.onkey(l_paddle.move_paddle_down, "s")

game_is_on = True
ball_speed = 1
while game_is_on:
    sleep_time = round(0.1/ball_speed, 4)
    ball.move()
    time.sleep(sleep_time)
    screen.update()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball_speed += 0.1

    # right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball_speed = 1
    # left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball_speed = 1
screen.exitonclick()
