from turtle import Turtle

FONT = ("Courier", 14, "bold")
COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(COLOR)
        self.goto(position)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.score, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
