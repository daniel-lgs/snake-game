from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("gray10")
my_screen.title("Snake Game!")
my_screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_score_board = ScoreBoard()

game_is_on = True

my_screen.listen()
my_screen.onkey(my_snake.turn_east, "Right")
my_screen.onkey(my_snake.turn_north, "Up")
my_screen.onkey(my_snake.turn_west, "Left")
my_screen.onkey(my_snake.turn_south, "Down")

while game_is_on:
    # Snake movement and frame update
    my_snake.walk()
    my_screen.update()
    time.sleep(0.1)

    # Collision with own tail
    for each_segment in my_snake.segments[3:]:
        if my_snake.head.distance(each_segment) < 20:
            my_score_board.reset_score()
            my_snake.reset_snake()

    # Collision with food
    if my_snake.head.distance(my_food) < 10:
        my_food.refresh()
        my_score_board.score += 1
        my_score_board.refresh()
        my_snake.extend()

    # Collision with borders
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280:
        my_score_board.reset_score()
        my_snake.reset_snake()
    elif my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        my_score_board.reset_score()
        my_snake.reset_snake()

    # Prevents the possibility of walking in the opposite direction of the head
    my_snake.clean_heads_per_interation()

my_screen.exitonclick()
