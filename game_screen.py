"""Game screen from turtle data"""
from turtle import Screen
screen = Screen()
screen.setup(width=600, height=600)
# animation off
screen.tracer(0)
# listen to events such as key events
screen.listen()
