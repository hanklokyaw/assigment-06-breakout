from turtle import Turtle, Screen

class Brick(Turtle):

    def __init__(self):
        super().__init__()
        self.all_bricks = []
        self.hideturtle()
        self.screen = Screen()

    def create_bricks(self):
        for i in range(-360,370,70):
            new_brick = Turtle("square")
            new_brick.shapesize(stretch_wid=1, stretch_len=3)
            new_brick.penup()
            new_brick.color("white")
            new_brick.x = i
            new_brick.y = 200
            self.all_bricks.append(new_brick)

    def update_bricks(self):
        for i in self.all_bricks:
            i.goto(i.x,i.y)
            print(f"X - {i.x}")
            print(f"Y - {i.y}")

    def clear_bricks(self):
        self.reset()