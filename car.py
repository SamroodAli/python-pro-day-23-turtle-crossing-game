"""Car module"""
import random
from turtle import Turtle

CAR_COLORS = ["blue", "dark blue", "red", "crimson", "orange red", "maroon", "indigo", "dark violet", "gold", "yellow",
              "green"]
CAR_LENGTH = [2, 3, 4]


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color(random.choice(CAR_COLORS))
        self.shapesize(stretch_len=random.choice(CAR_LENGTH))
        self.setheading(180)
        self.length = self.shapesize()[1]
        self.crash_distance = self.get_crash_distance()

    def move(self):
        self.forward(20)

    def get_crash_distance(self):
        if self.length == 2:
            return 11
        elif self.length == 3:
            return 21
        elif self.length == 4:
            return 31
