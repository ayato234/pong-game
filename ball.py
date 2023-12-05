from turtle import Turtle
import random

SHAPE = "circle"
COLOR = "white"
DISTANCE = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()
        self.x_factor = 0
        self.y_factor = 0
        self.start = None
        self.new_ball = None
        self.speed = 0
        self.reset_ball()
        self.in_game = False

    def reset_ball(self):
        self.home()
        self.x_factor = random.choice([-1, 1])
        self.y_factor = random.choice([-1, 1])
        self.start = False
        self.new_ball = True
        self.speed = DISTANCE

    def start_game(self):
        self.start = True
        self.in_game = True

    def get_new_ball(self):
        if not self.in_game:
            self.reset_ball()

    def move(self):
        new_x = self.xcor() + self.x_factor * self.speed
        new_y = self.ycor() + self.y_factor * self.speed
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_factor *= -1

    def bounce_paddle(self):
        self.x_factor *= -1

    def increase_speed(self):
        self.speed += 1
