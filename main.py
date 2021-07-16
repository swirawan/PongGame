from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Simple Pong Game")
screen.tracer(0)

left_paddle = Paddle(-350)
right_paddle = Paddle(350)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle.
    if ball.xcor() > 320 and ball.distance(right_paddle.return_pos()) < 50 \
            or ball.distance(left_paddle.return_pos()) < 50 \
            and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses.
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    # Detect L paddle misses.
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
