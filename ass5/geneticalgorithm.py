#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genetic algorithm class used to calculate necessary values for genetic algorithm simulations

Version:  69.420
Author:   MormonJesus69420
Date:     Yes, please
"""
from math import sqrt, fabs
from random import random, randint
from typing import List

from box import Box


class GeneticAlgorithm:
    def __init__(self, x=3, y=4):
        self.x = x
        self.y = y

    def calculate_fitness(self, population: List[Box]) -> None:
        for box in population:
            self._correct_quadrant_check(box)
            self._least_effort_check(box)

            # Want fitness to be positive, but harshly punished.
            if box.fitness < 0:
                box.fitness = fabs(box.fitness / 100)

        # Sort according to fitness, best first.
        population.sort(key=lambda box: box.fitness, reverse=True)

    def _correct_quadrant_check(self, box: Box) -> None:
        box.fitness += 10 if self._is_past_x(box.x) else -15
        box.fitness += 10 if self._is_past_y(box.y) else -15
        box.fitness += 50 if self._is_past_x(box.x) and self._is_past_y(box.y) else - 75

    def _least_effort_check(self, box: Box) -> None:
        if not self._is_past_x(box.x) or not self._is_past_y(box.y):
            return  # Do not reward if not in the right quadrant

        # Calculate distance
        distance = sqrt((self.x - box.x) ** 2 + (self.y - box.y) ** 2)

        # To reward lowest distance, add 100/distance.
        # Thus lower distance gives higher number
        if distance < 0.009:
            box.fitness = 10 ** 10
        else:
            box.fitness += 100 / (distance/10)

    def _is_past_x(self, x: float) -> bool:
        return x >= self.x

    def _is_past_y(self, y: float) -> bool:
        return y >= self.y

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

    def mutate_random(self, population: List[Box], no_mutations: int):
        for _ in range(no_mutations):
            if randint(0, 1) == 0:
                population[randint(0, len(population) - 1)].mutate_x()
            else:
                population[randint(0, len(population) - 1)].mutate_y()