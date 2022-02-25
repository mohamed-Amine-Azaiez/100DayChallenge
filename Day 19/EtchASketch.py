from turtle import Turtle, Screen

tim = Turtle()
screen=Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_r():
    tim.right(10)
def turn_l():
    tim.left(10)
def clear():
    tim.goto(0,0)
    tim.clear()

screen.listen()
screen.onkey(key="z",fun=move_forwards)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="d",fun=turn_r)
screen.onkey(key="q",fun=turn_l)
screen.onkey(key="c",fun=clear)



screen.exitonclick()