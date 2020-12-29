""""Scoreboard class to track player level"""
from turtle import Turtle
SCOREBOARD_POSITION = (0, 255)
FONT= ("Courier", 20, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.update_level()

    def update_level(self):
        self.write(arg=f"Level : {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()