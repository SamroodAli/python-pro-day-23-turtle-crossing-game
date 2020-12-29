"""Traffic management module"""
from car import Car
import random


class Traffic:
    def __init__(self):
        self.roads = []
        self.initialise_roads()
        self.cars = []
        super().__init__()

    def start_traffic(self):
        self.new_car()
        self.move_car()
        self.remove_crossed_cars()

    def new_car(self):
        lane = self.new_road()
        new_car = Car()
        new_car.goto(300, lane)
        self.cars.append(new_car)

    def initialise_roads(self):
        for lane in range(-240, 211, 25):
            self.roads.append(lane)

    def move_car(self):
        for car in self.cars:
            car.move()

    def remove_crossed_cars(self):
        for car in self.cars:
            if car.xcor() < -350:
                self.cars.remove(car)

    def new_road(self):
        chosen_road = random.choice(self.roads)
        self.roads.remove(chosen_road)
        if len(self.roads) == 0:
            self.initialise_roads()
        return chosen_road
