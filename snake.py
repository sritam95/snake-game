from turtle import Turtle
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
# self.list_of_turtles = [t1, t2, t3]
class Snake:
    def __init__(self):
        x = 0
        self.list_of_turtles = [t1, t2, t3]
        for i in self.list_of_turtles:
            i.shape("square")
            i.color("white")
            i.penup()
            i.goto(x,0)
            x -= 20
    
    def move(self):
        for a in range(len(self.list_of_turtles)-1,0,-1):
            t_nextx=self.list_of_turtles[a-1].xcor()
            t_nexty=self.list_of_turtles[a-1].ycor()
            self.list_of_turtles[a].goto(t_nextx,t_nexty)
    
        self.list_of_turtles[0].forward(20)
    
    def up(self):
        if self.list_of_turtles[0].heading()!=270:
            self.list_of_turtles[0].setheading(90)
            
    def down(self):
        if self.list_of_turtles[0].heading()!=90:
            self.list_of_turtles[0].setheading(270)
            
    def left(self):
        if self.list_of_turtles[0].heading()!=0:
            self.list_of_turtles[0].setheading(180)
            
    def right(self):
        if self.list_of_turtles[0].heading()!=180:
            self.list_of_turtles[0].setheading(0)
    
    def add_turtle(self):
        new_t=Turtle()
        new_t.penup()
        postion=self.list_of_turtles[-1].position()
        new_t.goto(postion)
        new_t.shape("square")
        new_t.color("white")
        self.list_of_turtles.append(new_t)
        
    def reset(self):
        # for i in range(3,len(self.list_of_turtles)-1):
        #     self.list_of_turtles.pop(i)
        me=self.list_of_turtles[3:]
        for i in me:
            i.hideturtle()
        self.list_of_turtlesa=self.list_of_turtles[:3]
        self.list_of_turtles=self.list_of_turtlesa
        # for i in self.list_of_turtles:
        #     i.hideturtle()
        snake = Snake()
        
    
        