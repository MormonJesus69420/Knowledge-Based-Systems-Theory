#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shpider Editor

Coordinate class representing coordinates on the map. Contains get_neighbours
method that returns a list of valid neighbouring tiles.

Version:  69.420
Author:   MormonJesus69420
Date:     Yes, please
"""


class Coordinate:
    max_x = 5
    max_y = 8
    x = 0
    y = 0

    def __init__(self, x, y):
        """if max_x is not None:
            self.max_x = max_x
        if max_y is not None:
            self.max_y = max_y"""
        self.x = x
        self.y = y

    def get_left(self):
        if self.x > 0:
            return Coordinate(self.x - 1, self.y)

    def get_right(self):
        if self.x < self.max_x:
            return Coordinate(self.x + 1, self.y)

    def get_up(self):
        if self.y > 0:
            return Coordinate(self.x, self.y - 1)

    def get_down(self):
        if self.y < self.max_y:
            return Coordinate(self.x, self.y + 1)

    def get_neighbours(self):
        # Get neighbours, some can be None
        neigh = [self.get_up(), self.get_right(),
                 self.get_down(), self.get_left()]

        # Create new list without None elements from neigh list
        return [x for x in neigh if x is not None]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def to_string(self):
        return "x: {}, y: {}, max_x: {}, max_y: {}".format(
                self.x, self.y, self.max_x, self.max_y)
