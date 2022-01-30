from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x=side, y=0)
        self.setheading(90)

    def go_up(self):
        if self.ycor() < 250:
            self.fd(20)

    def go_down(self):
        if self.ycor() > -240:
            self.bk(20)

