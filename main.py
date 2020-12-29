"""Main game file"""
import time
from game_screen import screen
from player import Player
from traffic_management import Traffic


# game instances
player = Player()
traffic = Traffic()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    traffic.start_traffic()
screen.exitonclick()
