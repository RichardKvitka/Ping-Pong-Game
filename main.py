from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()


screen.listen()

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Right paddle misses the ball
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_position()
        ball.bounce_x()



    #Left paddle misses the ball
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_position()
        ball.bounce_x()


screen.exitonclick()
