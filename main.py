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

while is_game_on:
    screen.update()
    time.sleep(traffic.speed)
    traffic.start_traffic()
# detect collision with cars
    for car in traffic.cars:
        if green_turtle.ycor() == (car.lane-5) and green_turtle.distance(car) <= car.crash_distance:
            scoreboard.game_over()
            is_game_on = False
# passing the level
    if green_turtle.ycor() >= 255:
        green_turtle.reset_position()
        scoreboard.level_up()
        traffic.increase_speed()
    screen.update()
screen.exitonclick()

