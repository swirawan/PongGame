from turtle import Turtle


class Paddle:
    def __init__(self, x_position):
        super().__init__()
        self.paddle_segments = []
        self.create_paddle(x_position)
        self.paddle = self.paddle_segments[0]

    def create_paddle(self, x_position):
        paddle = Turtle(shape="square")
        paddle.color("white")
        paddle.penup()
        paddle.goto(x=x_position, y=0)
        paddle.shapesize(stretch_wid=1, stretch_len=5)
        paddle.setheading(90)
        self.paddle_segments.append(paddle)

    def up(self):
        self.paddle.forward(20)

    def down(self):
        self.paddle.backward(20)

    def return_pos(self):
        return self.paddle.position()
