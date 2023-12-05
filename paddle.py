from turtle import Turtle

SHAPE = "square"
COLOR = "white"
FACTOR_WIDTH = 5
FACTOR_LENGTH = 0.5
DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.color(COLOR)
        self.shapesize(stretch_wid=FACTOR_WIDTH, stretch_len=FACTOR_LENGTH)
        self.goto(starting_position)

    def move_up(self):
        new_y = self.ycor() + DISTANCE
        self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - DISTANCE
        self.sety(new_y)
