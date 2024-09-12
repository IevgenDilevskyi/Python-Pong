from turtle import Screen
import time
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")
player_one = Paddle((350, 0))
player_two = Paddle((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(player_one.up, "Up")
screen.onkey(player_one.down, "Down")
screen.onkey(player_two.up, "w")
screen.onkey(player_two.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()










screen.exitonclick()
