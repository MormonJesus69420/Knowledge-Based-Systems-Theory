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
    cost = np.array([[1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1],
                     [1, 1, 1, 1, 1, 1]])

    def depth_first_search(start, end):
        # Define search stack S
        S = [start]
        # Define visited stack H
        H = list()
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
                return
            else:
                # Get neighbours in array
                neigh = i.get_neighbours()
                # Add unvisited neighbours to S
                S.extend([cord for cord in neigh if cord not in H])



# Call method static way
Search.depth_first_search(c.Coordinate(1,0), c.Coordinate(4, 7))