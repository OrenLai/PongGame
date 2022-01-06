from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_y(self):
        """change the y direction of the ball when the ball hit top or bottom wall"""
        self.move_y *= -1

    def bounce_x(self):
        """change the x direction , and increase the speed slightly by decrease the sleep time of the while loop"""
        self.move_x *= -1
        self.move_speed *= 0.9

    def back_to_center(self):
        """ move the ball back to the center and reset the speed """
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
