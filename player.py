"""Player data using turtle module"""
from turtle import Turtle, onkey
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
        self.event_listener()

    def move_up(self):
        self.forward(25)
        print(self.pos())

    def move_down(self):
        self.backward(25)

    def event_listener(self):
        onkey(key="Up", fun=self.move_up)
        onkey(key="Down", fun=self.move_down)
