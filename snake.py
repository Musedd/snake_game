import time
import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.spawn_Snake()
        self.snake_head = self.segments[0]

    def spawn_Snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move_Snake(self):
        for sna_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[sna_num - 1].xcor()
            new_y = self.segments[sna_num - 1].ycor()
            self.segments[sna_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    def move_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    def move_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    def move_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def add_segment(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color("black")
        snake_part.penup()
        snake_part.goto(position)
        self.segments.append(snake_part)

    def extend(self):
        self.add_segment(self.segments[-1].position())

