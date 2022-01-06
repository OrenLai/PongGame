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
        if self.ycor() < 270:
            self.goto(self.xcor(), self.ycor() + 30)

    def down(self):
        if self.ycor() > -270:
            self.goto(self.xcor(), self.ycor() - 30)
