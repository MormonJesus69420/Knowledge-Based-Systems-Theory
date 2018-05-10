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
    length = 5

    def __init__(self, chromosome: BitArray):
        self.x_chromosome = chromosome[0:self.length]
        self.y_chromosome = chromosome[self.length:self.length * 2]

    @staticmethod
    def crossover(box1: 'Box', box2: 'Box') -> List['Box']:
        length = Box.length

        cutoff = randint(1, length - 1)
        x_1 = box1.x_chromosome[0:cutoff] + box2.x_chromosome[cutoff:length]
        x_2 = box2.x_chromosome[0:cutoff] + box1.x_chromosome[cutoff:length]

        cutoff = randint(1, length - 1)
        y_1 = box1.y_chromosome[0:cutoff] + box2.y_chromosome[cutoff:length]
        y_2 = box2.y_chromosome[0:cutoff] + box1.y_chromosome[cutoff:length]

        return [Box(BitArray(x_1 + y_1)), Box(BitArray(x_2 + y_2))]

    def mutate(self):
        self.x_chromosome.invert(randint(0, self.length - 1))
        self.y_chromosome.invert(randint(0, self.length - 1))


b1 = Box(BitArray('0b1111111111'))
b2 = Box(BitArray('0b0000000000'))

print(BitArray('0b11111').int)

new = Box.crossover(b1, b2)

b1 = new[0]
b2 = new[1]

print(b1.x_chromosome.bin)
print(b1.y_chromosome.bin)
print(b2.x_chromosome.bin)
print(b2.y_chromosome.bin)

b1.mutate()

print(b1.x_chromosome.bin)
print(b1.y_chromosome.bin)
