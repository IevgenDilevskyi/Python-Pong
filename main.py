from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")
player_one = Paddle((350, 0))
player_two = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player_one.up, "Up")
screen.onkey(player_one.down, "Down")
screen.onkey(player_two.up, "w")
screen.onkey(player_two.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(player_one) < 50 and ball.xcor() > 320 or ball.distance(player_two) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect 1st player miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect 2nd player miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
