from turtle import Turtle

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_MOVE_DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.heads_per_iteration = [EAST]

    def new_segment(self):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("chartreuse")
        self.segments.append(segment)

    def create_snake(self):
        for each_position in INITIAL_POSITIONS:
            self.new_segment()
            self.segments[-1].setposition(each_position)

    def walk(self):
        for index_seg in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[index_seg - 1].position()
            self.segments[index_seg].setposition(new_position)
        self.head.forward(SNAKE_MOVE_DISTANCE)

    def extend(self):
        self.new_segment()

    def turn_east(self):
        if WEST not in self.heads_per_iteration:
            self.head.setheading(EAST)
            self.heads_per_iteration.append(EAST)

    def turn_north(self):
        if SOUTH not in self.heads_per_iteration:
            self.head.setheading(NORTH)
            self.heads_per_iteration.append(NORTH)

    def turn_west(self):
        if EAST not in self.heads_per_iteration:
            self.head.setheading(WEST)
            self.heads_per_iteration.append(WEST)

    def turn_south(self):
        if NORTH not in self.heads_per_iteration:
            self.head.setheading(SOUTH)
            self.heads_per_iteration.append(SOUTH)

    def clean_heads_per_interation(self):
        current_prohibited = self.heads_per_iteration[-1]
        self.heads_per_iteration.clear()
        self.heads_per_iteration.append(current_prohibited)

    def reset_snake(self):
        for segment in self.segments:
            segment.hideturtle()
        self.__init__()
