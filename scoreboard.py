from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.color("white")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()
