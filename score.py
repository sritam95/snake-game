from turtle import Turtle
class Score:
    def __init__(self):
        self.score = Turtle()
        self.sc=0
        self.highscore = 0
        self.score.penup()
        self.score.goto(0,270)
        self.score.color("white")
        self.score.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.score.clear()
        self.score.write(f"score: {self.sc} highscore: {self.highscore}", align="center", font=("arial","20","normal"))
    
    def update(self):
        self.sc+=1
        self.update_score()
        
    def game_over(self):
        # self.score.home()
        # self.score.write("GAME OVER", align="center", font=("arial","20","normal"))
        if self.sc > self.highscore:
            self.highscore = self.sc
            with open("sritam.txt",'w') as hs:
                hs.write(f"{self.highscore}")
        self.sc = 0
        self.update_score()
        
        
    
