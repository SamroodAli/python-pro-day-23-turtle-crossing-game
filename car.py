"""Car module"""
import random
from turtle import Turtle

CAR_COLORS = ["blue", "dark blue", "red", "crimson", "orange red", "maroon", "indigo", "dark violet", "gold", "yellow",
              "green"]
CAR_LENGTH = [2, 3]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(CAR_COLORS))
        self.shapesize(stretch_len=random.choice(CAR_LENGTH))
        self.setheading(180)
        self.length= self.shapesize()[1]

    def move(self):
        self.forward(20)
