#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shpider Editor

Search class, does what it says on the tin

Version:  69.420
Author:   MormonJesus69420
Date:     Yes, please
"""

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
        S = [start]
        H = list()
        matrix = np.zeros((9, 6), dtype=int)

        while S:
            i = S.pop()
            H.append(i)
            matrix[i.x, i.y] = 1

            if i is end:
                return matrix
            else:
                neigh = i.get_neighbours()
                S.extend([cord for cord in neigh if cord not in H])

            print(matrix)

        return matrix


Search.depth_first_search(c.Coordinate(0, 1), c.Coordinate(4, 7))