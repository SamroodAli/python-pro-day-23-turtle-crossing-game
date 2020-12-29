"""Player data using turtle module"""
from turtle import Turtle
STARTING_POSITION = (0, -270)


class Player(Turtle):
    """Player class"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
