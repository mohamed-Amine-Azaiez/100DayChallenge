from turtle import Turtle,Screen
import random
import turtle

screen=Screen()

screen.setup(width=500,height=400)
on=False
bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color")

colors=["red","yellow","orange","green","blue","purple"]
y_position=[-125,-75,-25,25,75,125]
all_turtles=[]
if bet:
    on=True

for i in range(0,6):
    t1 = Turtle()
    t1.shape("turtle")
    t1.color(colors[i])
    t1.penup()
    t1.goto(x=-230,y=y_position[i])
    all_turtles.append(t1)
while on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            on=False
            win=turtle.pencolor()
            if win == bet.lower():
                print("You've Won!")
            else:
                print("You've Lost!")
                print(f"{win} has won")
        distance=random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()