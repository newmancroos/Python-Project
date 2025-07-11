import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # default is 20x20 we made them 10x10
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rnd_x = random.randint(-280, 280)
        rnd_y = random.randint(-280, 280)
        self.goto(rnd_x, rnd_y)

