from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()

        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_coordinate = self.xcor() + self.x_move
        y_coordinate = self.ycor() + self.y_move
        self.goto(x=x_coordinate, y=y_coordinate)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.move_speed = 0.1
        self.goto(x=0, y=0)
        self.bounce_x()
