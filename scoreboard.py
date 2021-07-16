from turtle import Turtle

FONT = ("Courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, move=False, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, move=False, align="center", font=FONT)

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.write_score()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.write_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", move=False, align="center", font=FONT)