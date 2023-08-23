from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.new_x = 0
        self.new_y = 0
        self.displacement_x = 10
        self.displacement_y = 10
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.new_x = self.xcor() + self.displacement_x
        self.new_y = self.ycor() + self.displacement_y
        self.goto(self.new_x, self.new_y)

    def bounce_y(self):
        self.displacement_y *= -1

    def bounce_x(self):
        self.displacement_x *= -1

    def reset_position(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()

        self.displacement_x *= -1
        self.displacement_y *= -1
