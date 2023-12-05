from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
r_score = Scoreboard((30, 270))
l_score = Scoreboard((-30, 270))


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(ball.start_game, "space")
screen.onkey(ball.get_new_ball, "n")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)

    if ball.new_ball and ball.start:
        ball.move()

        # Detect collision with wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_wall()

        # Detect collision with paddle
        if ((330 < ball.xcor() < 350 and ball.distance(r_paddle) < 50)
                or (-350 < ball.xcor() < -330 and ball.distance(l_paddle) < 50)):
            ball.bounce_paddle()
            ball.increase_speed()

        # Detect goal
        if ball.xcor() > 390:
            l_score.increase_score()
            ball.in_game = False
            ball.new_ball = False
        elif ball.xcor() < -390:
            r_score.increase_score()
            ball.in_game = False
            ball.new_ball = False

screen.exitonclick()
