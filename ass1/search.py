#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Search class, does what it says on the tin

Version:  69.420
Author:   MormonJesus69420
Date:     Yes, please
"""

import matplotlib.pyplot as plt
import coordinate as c
import numpy as np
import maze as m
import math


class Search:
    def __init__(self):
        pass

    @staticmethod
    def cost(coordinate):
        return m.cost_array[coordinate.y, coordinate.x]

    @staticmethod
    def estimated_cost(start, end):
        # return abs(start.x - end.x) + abs(start.y - end.y)
        return math.hypot(end.x - start.x, end.y - start.y)

    def a_star(self, start, stop):
        # Define list of evaluated elements
        searched = []
        # Define list of elements to test
        search = [start]
        # Define dictionary of element parents
        parents = {}

        # Define matrix of g values for elements, normally infinitely big
        g = np.full((m.size, m.size), np.inf)
        # G value for start is zero
        g[start.y, start.x] = 0

        # Define matrix of f values for elements, normally infinitely big
        f = np.full((m.size, m.size), np.inf)
        # F value for start is heuristic value
        f[start.y, start.x] = self.estimated_cost(start, stop)

        while search:
            # Sort search according to F values of elements, smallest on back
            search.sort(key=lambda node: f[node.y, node.x], reverse=True)
            # Pop the smallest element
            current = search.pop()
            # Add current element to evaluated element list
            searched.append(current)

            # If current is goal, then stop
            if current == stop:
                return self.make_path(parents, current)

            # For all neighbours of current that were not evaluated so far
            for n in [x for x in current.neighbours() if x not in searched]:
                # Add neighbour to test stack if not already there
                if n not in search:
                    search.append(n)

                # Find new g value for neighbour
                temp_g = g[current.y, current.x] + self.cost(n)

                # Skip if new g value is larger than or equal to previous
                if temp_g >= g[n.y, n.x]:
                    continue

                # Found better path, set parent of neighbour to current
                parents[n] = current
                # Update g value for neighbour
                g[n.y, n.x] = temp_g
                # Update f value for neighbour
                f[n.y, n.x] = temp_g + self.estimated_cost(n, stop)

        # No path exists, return empty path
        return m.cost_array

    @staticmethod
    def make_path(parents, current):
        # Add current element to path
        m.cost_array[current.y, current.x] = m.path

        # Go backwards in parent hierarchy
        while current in parents:
            current = parents[current]
            m.cost_array[current.y, current.x] = m.path

        return m.cost_array

    def depth_first_search(self, start, end):
        return self.default_search(start, end, True)

    def breadth_first_search(self, start, end):
        return self.default_search(start, end, False)

    @staticmethod
    def default_search(start, end, is_depth_first):
        # Define search stack search
        search = [start]
        # Define visited stack searched
        searched = []
        # Define 9x6 matrix for showing visited nodes, 0 not visited, 1 visited
        matrix = np.zeros((9, 6), dtype=int)

        while search:
            # Pop last element from search
            i = search.pop()
            # Add element to searched
            searched.append(i)
            # Mark element as visited in matrix
            matrix[i.y][i.x] = 1

            # If element is equal to end goal, stop and return matrix
            if i == end:
                return matrix
            else:
                # Get ns in array
                neigh = i.neighbours()
                # Add unvisited ns to search
                if is_depth_first:
                    search.extend([x for x in neigh if x not in searched])
                else:
                    search = [x for x in neigh if x not in searched] + search

        # search stack empty, no result.
        return matrix


s = Search()

# temp = s.depth_first_search(c.Coordinate(1, 0), c.Coordinate(4, 7))
# plt.imshow(temp)
# plt.show()
#
# temp = s.breadth_first_search(c.Coordinate(1, 0), c.Coordinate(4, 7))
# plt.imshow(temp)
# plt.show()

temp = s.a_star(c.Coordinate(51, 0, m.size - 1, m.size - 1), c.Coordinate(51, 100, m.size - 1, m.size - 1))
plt.imshow(temp)
plt.show()
