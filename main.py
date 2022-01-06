from turtle import Screen
from middle_line import MiddleLine
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

# draw the middle line
mid_line = MiddleLine()
mid_line.draw()
# create peddles
left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))

scoreboard_left = Scoreboard((-50, 280))
scoreboard_right = Scoreboard((50, 280))

ball = Ball()
screen.update()
screen.listen()

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340 or ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # detect the ball go over the walls
    if ball.xcor() > 400:
        scoreboard_left.add_score()
        ball.back_to_center()

    if ball.xcor() < -400:
        scoreboard_right.add_score()
        ball.back_to_center()

screen.exitonclick()
