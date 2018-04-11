#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shpider Editor

Search class, does what it says on the tin

Version:  69.420
Author:   MormonJesus69420
Date:     Yes, please
"""

import matplotlib.pyplot as plt
import coordinate as c
import numpy as np


class Search:
    cost_array = np.array([[1, 1, 2, 2, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 3, 3, 2, 1],
                     [1, 1, 1, 2, 2, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 2, 3, 3, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 3, 1, 1, 1, 1]])


    def cost(coordinate):
        return Search.cost_array[coordinate.y][coordinate.x]

    def estimated_cost(start, end):
        return abs(start.x - end.x) + abs(start.y - end.y)

    def a_star(start, stop):
        # Define list of evaluated elements
        H = []
        # Define list of elements to test
        S = [start]
        # Define dictionary of element parents
        parents = {}

        # Define matrix of g values for elements, normally infinitely big
        Gs = np.full((9, 6), np.inf)
        # G value for start is zero
        Gs[start.y, start.x] = 0

        # Define matrix of f values for elements, normally infinitely big
        Fs = np.full((9, 6), np.inf)
        # F value for start is heuristic value
        Fs[start.y, start.x] = Search.estimated_cost(start, stop)

        while S:
            # Sort S according to F values of elements, smallest on back
            S.sort(key=lambda c: (Fs[c.y, c.x]), reverse=True)
            # Pop the smallest element
            current = S.pop()
            # Add current element to evaluated element list
            H.append(current)

            # If current is goal, then stop
            if current == stop:
                return Search.makePath(parents, current)

            # For all neighbours of current that were not evaluated so far
            for n in [c for c in current.get_neighbours() if c not in H]:
                # Add neighbour to test stack if not already there
                if n not in S:
                    S.append(n)

                # Find new g value for neighbour
                temp_g = Gs[current.y, current.x] + Search.cost(n)

                # Skip if new g value is larger than or equal to previous
                if temp_g >= Gs[n.y, n.x]:
                    continue

                # Found better path, set parent of neighbour to current
                parents[n] = current
                # Update g value for neighbour
                Gs[n.y, n.x] = temp_g
                # Update f value for neighbour
                Fs[n.y, n.x] = temp_g + Search.estimated_cost(n, stop)

        # No path exists, return empty path
        return np.zeros((9, 6), dtype=int)

    def makePath(parents, current):
        # Create empty path matrix
        matrix = np.zeros((9, 6), dtype=int)
        # Add current element to path
        matrix[current.y, current.x] = 1

        # Go backwards in parent hierarchy
        while current in parents:
            current = parents[current]
            matrix[current.y, current.x] = 1

        return matrix

    def depth_first_search(start, end):
        return Search.default_search(start, end, True)

    def breadth_first_search(start, end):
        return Search.default_search(start, end, False)

    def default_search(start, end, is_depth_first):
        # Define search stack S
        S = [start]
        # Define visited stack H
        H = []
        # Define 9x6 matrix for showing visited nodes, 0 not visited, 1 visited
        matrix = np.zeros((9, 6), dtype=int)

        while S:
            # Pop last element from S
            i = S.pop()
            # Add element to H
            H.append(i)
            # Mark element as visited in matrix
            matrix[i.y][i.x] = 1

            # If element is equal to end goal, stop and return matrix
            if i == end:
                plt.imshow(matrix)
                return H
            else:
                # Get ns in array
                neigh = i.get_neighbours()
                # Add unvisited ns to S
                if is_depth_first:
                    S.extend([cord for cord in neigh if cord not in H])
                else:
                    S = [cord for cord in neigh if cord not in H] + S

        # S stack empty, no result.
        plt.imshow(matrix)
        return H

#Search.depth_first_search(c.Coordinate(1, 0), c.Coordinate(4, 7))
#Search.breadth_first_search(c.Coordinate(1, 0), c.Coordinate(4, 7))

temp = Search.a_star(c.Coordinate(1, 0), c.Coordinate(4, 7))
plt.imshow(temp)
