"""Main game file"""
import time
from game_screen import screen
from player import Player



# game instances
player = Player()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
screen.exitonclick()
