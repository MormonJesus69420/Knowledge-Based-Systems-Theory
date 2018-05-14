#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sets up and runs simulation

Version:  69.420
Author:   MormonJesus69420
Date:     Yes, please
"""
from random import randint

from bitstring import BitArray

from box import Box
from geneticalgorithm import GeneticAlgorithm

pop = [Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       Box(BitArray(uint=randint(0, 2 ** 24 - 1), length=24)),
       ]

# Initialize genetic algorithm
ga = GeneticAlgorithm(3, 4)

for generation in range(1, 10000):
    if generation % 4 == 0:
        ga.mutate_random(pop, 100)

    ga.calculate_fitness(pop)

    if len(pop) > 5000:
        pop = pop[:1000]

    pop = ga.roulette(pop)

    print(f'Generation {generation} best specimen -> {pop[0].x} {pop[0].y} '
          f'x chromosome: {pop[0].x_chromosome.bin} '
          f'y chromosome: {pop[0].y_chromosome.bin} ')

    if pop[0].x == ga.x and pop[0].y == ga.y:
        print(f'Optimal found in generation {generation}, -> '
              f'x chromosome: {pop[0].x_chromosome.bin} '
              f'y chromosome: {pop[0].y_chromosome.bin}')
        break
