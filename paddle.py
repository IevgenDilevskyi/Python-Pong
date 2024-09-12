from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.shapesize(5, 1)
        self.goto(coord)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


