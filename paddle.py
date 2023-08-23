from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor=0):
        self.x_cor = x_cor
        self.y_cor = y_cor
        super().__init__()
        self.speed(0)
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.x_cor, self.y_cor)


    def move_paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x_cor, new_y)

    def move_paddle_down(self):
        new_y = self.ycor() -  20
        self.goto(self.x_cor, new_y)
