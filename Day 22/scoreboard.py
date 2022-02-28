
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update()
        self.on = True
        
    def update(self):
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))



    def l_point(self):
        self.clear()
        self.l_score+=1
        self.update()
    def r_point(self):
        self.clear()
        self.r_score+=1
        self.update()
    
    def check(self):
        if self.l_score > 4:
            self.clear()
            self.goto(0,0)
            self.write("Game over. Left player wins",align="center",font=("Courier",18,"normal"))
            self.on = False
        elif self.r_score >4:
            self.clear()
            self.goto(0,0)
            self.write("Game over. Right player wins",align="center",font=("Courier",18,"normal"))
            self.on = False
            