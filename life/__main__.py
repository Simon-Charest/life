#!/usr/bin/python
# coding=utf-8

__author__ = 'Simon Charest'
__copyright__ = 'Copyright 2019, SLCIT inc.'
__credits__ = ['John Horton Conway']
__email__ = 'simoncharest@gmail.com'
__license__ = 'GPL'
__maintainer__ = 'Simon Charest'
__project__ = 'Game of Life'
__status__ = 'Developement'
__version__ = '1.0.0'

import os
import random
import time

ROWS = 16
COLS = 70
GENERATIONS = 999
DELAY = 0.1
LIVE_CELL = '☻'
DEAD_CELL = ' '
BORDER_TOP_LEFT = '╔'
BORDER_HORIZONTAL = '═'
BORDER_TOP_RIGHT = '╗'
BORDER_VERTICAL = '║'
BORDER_BOTTOM_LEFT = '╚'
BORDER_BOTTOM_RIGHT = '╝'


def main():
    current_generation = []
    next_generation = []

    initialize_matrix(COLS, ROWS, current_generation)
    initialize_matrix(COLS, ROWS, next_generation)

    for generation in range(GENERATIONS):
        print_matrix(COLS, ROWS, current_generation, generation, LIVE_CELL, DEAD_CELL, BORDER_TOP_LEFT,
                     BORDER_HORIZONTAL, BORDER_TOP_RIGHT, BORDER_VERTICAL, BORDER_BOTTOM_LEFT, BORDER_BOTTOM_RIGHT)
        process_next_generation(COLS, ROWS, current_generation, next_generation)
        current_generation, next_generation = next_generation, current_generation
        time.sleep(DELAY)

    input('Done: Press any key to quit')


def initialize_matrix(cols, rows, matrix):
    for y in range(rows):
        row = []
        for x in range(cols):
            if y == 0 or x == 0 or y == rows - 1 or x == cols - 1:
                row += [-1]
            else:
                if random.randint(0, 3) == 0:
                    row += [1]
                else:
                    row += [0]
        matrix += [row]


def print_matrix(cols, rows, matrix, generation, live_cell, dead_cell, border_top_left, border_horizontal,
                 border_top_right, border_vertical, border_bottom_left, border_bottom_right):
    os.system('clear')

    print('Game of life | Generation: ' + str(generation + 1))

    for y in range(rows):
        for x in range(cols):
            if matrix[y][x] == -1:
                if y == 0:
                    if x == 0:
                        print(border_top_left, end=' ')
                    elif x == cols - 1:
                        print(border_top_right, end=' ')
                    else:
                        print(border_horizontal, end=' ')
                elif y == rows - 1:
                    if x == 0:
                        print(border_bottom_left, end=' ')
                    elif x == cols - 1:
                        print(border_bottom_right, end=' ')
                    else:
                        print(border_horizontal, end=' ')
                elif x == 0 or x == cols - 1:
                    print(border_vertical, end=' ')
            elif matrix[y][x] == 1:
                print(live_cell, end=' ')
            else:
                print(dead_cell, end=' ')
        print('\n')


def process_next_generation(cols, rows, current_matrix, next_matrix):
    for y in range(1, rows - 1):
        for x in range(1, cols - 1):
            next_matrix[y][x] = process_neighbours(y, x, current_matrix)


def process_neighbours(x_current, y_current, matrix):
    count = 0

    for x in range(y_current - 1, y_current + 2):
        for y in range(x_current - 1, x_current + 2):
            if not (y == x_current and x == y_current):
                if matrix[y][x] != -1:
                    count += matrix[y][x]

    if matrix[x_current][y_current] == 1 and count < 2 or matrix[x_current][y_current] == 1 and count > 3:
        return 0

    if matrix[x_current][y_current] == 0 and count == 3:
        return 1

    else:
        return matrix[x_current][y_current]


main()
