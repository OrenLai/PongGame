from turtle import Screen
from middle_line import Middle_line
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

# draw the middle line
mid_line = Middle_line()
mid_line.draw()
# create peddles
left_paddle = Paddle((-380, 0))
right_paddle = Paddle((380, 0))


screen.update()
screen.listen()

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
