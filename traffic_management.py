"""Traffic management module"""
from car import Car
import random


class Traffic:
    def __init__(self):
        self.roads = []
        self.cars = []
        self.initialise_roads()
        super().__init__()

    def start_traffic(self):
        self.new_car()
        self.move_car()
        self.remove_crossed_cars()

    def new_car(self):
        new_car = Car()
        new_car.goto(300, random.choice(self.roads))
        self.cars.append(new_car)

    def initialise_roads(self):
        for lane in range(-240, 260, 25):
            self.roads.append(lane)

    def move_car(self):
        for car in self.cars:
            car.move()

    def remove_crossed_cars(self):
        for car in self.cars:
            if car.xcor() < -350:
                self.cars.remove(car)
