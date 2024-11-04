from turtle import Turtle, Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width =600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
game_is_on = True
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect Collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect Collision with Tail

    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()















screen.exitonclick()

