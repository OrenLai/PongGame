from turtle import Turtle


class Middle_line(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.pendown()
        self.hideturtle()
        self.pensize(5)
        self.speed(0)

    def draw(self):
        while self.ycor() < 300:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
