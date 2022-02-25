from mimetypes import read_mime_types
from turtle import Turtle,Screen
import time

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")
screen = Screen()

def draw(step,ang):
    for _ in range(step):
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()
    timmy_the_turtle.right(ang)
for _ in range(10) :
    draw(10,90)
    draw(10,90)
    draw(10,90)
    draw(10,135)
    draw(10,135)
    draw(10,135)
    draw(10,135)
    
screen.exitonclick()





