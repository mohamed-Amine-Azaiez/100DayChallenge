from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.high_score =0 
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update()
        

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} - High Score: {self.high_score}", align="center",font=("Arial",24,"normal"))

    def increase_score(self):
        self.score +=1
        self.update()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", align="center",font=("Arial",24,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score=0
        self.update()