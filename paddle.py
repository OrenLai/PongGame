from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.segments_left = []
        self.segments_right = []
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
