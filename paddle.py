from turtle import Turtle

paddle_left_position = [(-480, -20), (-480, 0), (-480, 20)]
paddle_right_position = [(480, -20), (480, 0), (480, 20)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.segments_left = []
        self.segments_right = []
        self.color("White")
        self.hideturtle()
        self.create_paddle(paddle_left_position, 1)
        self.create_paddle(paddle_right_position, 2)

    def create_paddle(self, position, player):
        for pos in position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(pos)
            if player == 1:
                self.segments_left.append(new_segment)
            else:
                self.segments_right.append(new_segment)

    def left_paddle_up(self):
        print("paddle up")
        for segment in self.segments_left:
            segment.setheading(90)
            segment.forward(20)


