#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genetic algorithm class used to calculate necessary values for genetic algorithm simulations

Version:  69.420
Author:   MormonJesus69420
Date:     Yes, please
"""
from random import random

from typing import List

from bitstring import BitArray

from box import Box

from math import ceil

class GeneticAlgorithm:

    def calculate_fitness(self, population: List[Box]) -> None:
        for box in population:
            self.correct_quadrant_check(box)
            self.least_effort_check(box)

    def correct_quadrant_check(self, box: Box) -> None:
        pass

    def least_effort_check(self, box: Box) -> None:
        pass

    def roulette(self, population: List[Box]) -> List[Box]:
        # Get total fitness
        total = sum(box.fitness for box in population)

        # Normalize fitness of each box to values 0-1
        [self._normalize_fitness(box, total) for box in population]

        # Create list of accumulated fitness scores
        acc = list()
        temp = 0.0
        for box in population:
            temp += box.fitness
            acc.append(temp)

        # Breed new population
        new_pop = list()
        for _ in range(0, len(population)):
            daddy = population[self._get_index(acc, random())]
            mommy = population[self._get_index(acc, random())]
            # Do not accept breeding with itself
            while daddy == mommy:
                mommy = population[self._get_index(acc, random())]
            babies = mommy.crossover(daddy)
            new_pop.append(babies[0])
            new_pop.append(babies[1])

        return new_pop

    def _normalize_fitness(self, box: Box, total_fitness: int) -> None:
        box.fitness /= total_fitness

    def _get_index(self, acc: List[float], percentage: float) -> int:
        for i in range(0, len(acc)):
            if percentage < acc[i]:
                return i

# Random population values guaranteed to be random
# pop = [Box(BitArray('0b1100011101000001')),
#        Box(BitArray('0b1001100101100011')),
#        Box(BitArray('0b1010101010100111')),
#        Box(BitArray('0b0111000001011111')),
#        Box(BitArray('0b1110111010000101')),
#        Box(BitArray('0b1110000011011011')),
#        Box(BitArray('0b1110001001101010')),
#        Box(BitArray('0b0100010100100011')),
#        Box(BitArray('0b1111010000101101')),
#        Box(BitArray('0b0110011101101011')),
#        Box(BitArray('0b0111101000111011')),
#        Box(BitArray('0b1100001010101000')),
#        ]

r = GeneticAlgorithm().roulette
pop = [Box(BitArray('0b1111111111111111')),
       Box(BitArray('0b0000000000000000')),
       Box(BitArray('0b0101010101010101')),
       Box(BitArray('0b1111111100000000')),
       ]

pop[0].fitness = 50
pop[1].fitness = 30
pop[2].fitness = 15
pop[3].fitness = 5

meh = r(pop)

for box in meh:
    print(box.x_chromosome.bin)
