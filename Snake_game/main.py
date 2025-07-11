from turtle import  Screen
import time
from  food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


game_is_on = True

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail

    snake_slice = snake.segments[1:]
    # for segment in snake.segments:
    for segment in snake_slice:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



# t2= Turtle()
# t2.shape("square")
# t2.color("white")
# # t2.setx(round(t1.xcor()) - 20)
# t2.goto(round(t1.xcor()) - 20,0)
#
# t3= Turtle()
# t3.shape("square")
# t3.color("white")
# # t3.setx(round(t2.xcor()) - 20)
# t3.goto(round(t2.xcor()) - 20,0)

screen.exitonclick()