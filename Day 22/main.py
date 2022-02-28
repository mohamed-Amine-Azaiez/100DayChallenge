from turtle import Turtle,Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard


screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle(350)
l_paddle=Paddle(-350)
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")

screen.onkeypress(l_paddle.go_up,"z")
screen.onkeypress(l_paddle.go_down,"s")


while scoreboard.on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()

    if (ball.distance(r_paddle)<50 and ball.xcor() >320) or (ball.distance(l_paddle)<50 and ball.xcor()< -320):
        
        ball.bounce_x()
    if ball.xcor()>380:
        ball.reset()
        scoreboard.l_point()
        scoreboard.check()
    if ball.xcor()<-380:
        ball.reset()
        scoreboard.r_point()
        scoreboard.check()

screen.exitonclick()