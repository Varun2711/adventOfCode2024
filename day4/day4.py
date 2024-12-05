# Advent of code 2024
# Day 4: Ceres Search
# find occurrences of xmas in a matrix

import math
import numpy as np
from scipy.spatial.transform import Rotation

# part 1
# need to check rows, columns, overlaps, reverse and diagonals (not just center)

crossword = []
xmas_count = 0
# import data
with open('../inputs/day4input.txt', 'r') as f:
    for line in f.readlines():
        crossword.append(list(line.rstrip()))


# check horizontal (rows)
for row in crossword:
    str_row = ''.join(row)
    xmas_count += str_row.count('XMAS') + str_row.count('SAMX')

print(xmas_count)

# check columns:

# first create transpose of word search matrix
# this makes all the columns into rows
for row in crossword:
    print(row)

transpose = [[crossword[j][i] for j in range(len(crossword))] for i in range(len(crossword[0]))]
        
# then count the occurrences in the rows of the transpose
for row in transpose:
    str_row = ''.join(row)
    xmas_count += str_row.count('XMAS') + str_row.count('SAMX')

print(xmas_count)


# now the hard part
# spent 3 hours on using matrix rotation.... (don't do it)

# 