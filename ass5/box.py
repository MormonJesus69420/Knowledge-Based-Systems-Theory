#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Box class represents a box that will move in a genetic algorithm simulation

Version:  69.420
Author:   MormonJesus69420
Date:     Yes, please
"""

from random import randint
from typing import List

from bitstring import BitArray


class Box:
    def __init__(self, chromosome: BitArray, length=12):
        self._fitness = 0
        self._length = length
        self.x_chromosome = chromosome[0:length]
        self.y_chromosome = chromosome[length:length * 2]

    def crossover(self, box: 'Box') -> List['Box']:
        cutoff = randint(1, self.length - 1)
        x_1 = self.x_chromosome[0:cutoff] + box.x_chromosome[cutoff:self.length]
        x_2 = box.x_chromosome[0:cutoff] + self.x_chromosome[cutoff:self.length]

        cutoff = randint(1, self.length - 1)
        y_1 = self.y_chromosome[0:cutoff] + box.y_chromosome[cutoff:self.length]
        y_2 = box.y_chromosome[0:cutoff] + self.y_chromosome[cutoff:self.length]

        return [Box(BitArray(x_1 + y_1)), Box(BitArray(x_2 + y_2))]

    def mutate_x(self):
        self.x_chromosome.invert(randint(0, self.length - 1))

    def mutate_y(self):
        self.y_chromosome.invert(randint(0, self.length - 1))

    def _set_fitness(self, fitness: int):
        self._fitness = fitness

    def _get_fitness(self):
        return self._fitness

    def _get_length(self):
        return self._length

    def _get_x(self):
        return self.x_chromosome.uint / 100.0

    def _get_y(self):
        return self.y_chromosome.uint / 100.0

    x = property(_get_x)
    y = property(_get_y)
    length = property(_get_length)
    fitness = property(_get_fitness, _set_fitness)
