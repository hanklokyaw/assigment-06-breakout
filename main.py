from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -260))
ball = Ball()
brick = Brick()
brick.create_bricks()
brick.update_bricks()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    #Detect collision with paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -240:
        ball.bounce_y()
        # print(ball.bounce_y())

    #Detect collision with brick
    for i in brick.all_bricks:
        if i.distance(ball) < 20:
            scoreboard.point()
            i.hideturtle()
            brick.all_bricks.remove(i)
            brick.update_bricks()
            brick.clear_bricks()
            # screen.update()
            if len(brick.all_bricks) == 0:
                game_is_on = False
                scoreboard.finished()

    #Detect paddle misses
    if ball.ycor() < -280:
        ball.reset_position()
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()