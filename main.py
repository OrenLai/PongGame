from turtle import Screen, Turtle
from middle_line import Middle_line
from paddle import Paddle
screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

# draw the middle line
mid_line = Middle_line()
mid_line.draw()
# create peddles
paddles = Paddle()

screen.update()
screen.listen()

screen.onkey(paddles.left_paddle_up(), "w")
# screen.onkey(paddles.left_paddle_down(), "s")
# screen.onkey(paddles.right_paddle_up(), "up")
# screen.onkey(paddles.right_paddle_down(), "down")


game_on = True

while game_on:
    screen.update()



screen.exitonclick()