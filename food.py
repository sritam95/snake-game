from turtle import Turtle
import random 

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.penup()
        self.speed("fastest")
        self.sritam_idea()
        
    def sritam_idea(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        