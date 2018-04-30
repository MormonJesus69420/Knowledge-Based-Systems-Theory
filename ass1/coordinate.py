#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coordinate class representing coordinates on the map. Contains get_neighbours
method that returns a list of valid neighbouring tiles.

Version:  69.420
Author:   MormonJesus69420
Date:     Yes, please
"""


class Coordinate:
    def __init__(self, x=0, y=0, max_x=5, max_y=8):
        self.max_x = max_x
        self.max_y = max_y
        self.x = x
        self.y = y

    def left(self):
        if self.x > 0:
            return Coordinate(self.x - 1, self.y, self.max_x, self.max_y)

    def right(self):
        if self.x < self.max_x:
            return Coordinate(self.x + 1, self.y, self.max_x, self.max_y)

    def up(self):
        if self.y > 0:
            return Coordinate(self.x, self.y - 1, self.max_x, self.max_y)

    def down(self):
        if self.y < self.max_y:
            return Coordinate(self.x, self.y + 1, self.max_x, self.max_y)

    def neighbours(self):
        # Get neighbours, some can be None
        neigh = [self.up(), self.right(),
                 self.down(), self.left()]

        # Create new list without None elements from neigh list
        return [x for x in neigh if x is not None]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def to_string(self):
        return "x: {}, y: {}, max_x: {}, max_y: {}".format(
                self.x, self.y, self.max_x, self.max_y)
