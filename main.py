from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Scoreboard

RIGHT = 350
LEFT = -350


paddle_right = Paddle(RIGHT)
paddle_left = Paddle(LEFT)
ball = Ball()
score = Scoreboard()

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ball.collide_top()
    if ball.distance(paddle_right) < 40 and ball.xcor() > 320 or ball.distance(paddle_left) < 40 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
