from turtle import Screen
from food import Food
from score import Score
from snake import Snake, t1
import time
s = Screen()
f = Food()

s.setup(600, 600)
s.title("MY SNAKE GAME")
s.bgcolor("purple")
s.listen()
s.tracer(0)
snake=Snake()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")
game_is_on = True
score=Score()

while game_is_on:
    s.update()
    time.sleep(0.2)
    snake.move()
    if t1.distance(f) <= 15:
        snake.add_turtle()
        score.update()
        f.sritam_idea()
    if t1.xcor() > 280 or t1.xcor() < -280 or t1.ycor() > 280 or t1.ycor() < -280:
        score.game_over()
        snake.reset()
    for k in snake.list_of_turtles[1:]:
        if t1.distance(k)<10:
             score.game_over()
             snake.reset()
    
        
        









s.exitonclick()