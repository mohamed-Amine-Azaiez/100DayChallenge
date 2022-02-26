
from turtle import Turtle
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            t=Turtle(shape="square")
            t.color("white")
            t.penup()
            t.goto(pos)
            self.segments.append(t)
    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            x=self.segments[seg-1].xcor()
            y=self.segments[seg-1].ycor()
            self.segments[seg].goto(x,y)
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)