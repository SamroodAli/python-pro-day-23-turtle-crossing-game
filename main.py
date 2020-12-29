"""Main game file"""
import time
from game_screen import screen
from player import Player
from traffic_management import Traffic
from scoreboard import ScoreBoard

# game instances
green_turtle = Player()
traffic = Traffic()
scoreboard = ScoreBoard()

is_game_on = True
move_speed = 0.1
while is_game_on:
    screen.update()
    time.sleep(move_speed)
    traffic.start_traffic()
# detect collision with cars
    for car in traffic.cars:
        distance = 20
        if green_turtle.distance(car) < distance:
            is_game_on = False
            scoreboard.game_over()
# passing the level
    if green_turtle.ycor() >= 255:
        green_turtle.reset_position()
        scoreboard.level_up()
screen.exitonclick()
