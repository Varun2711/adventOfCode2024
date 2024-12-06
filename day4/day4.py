# Advent of code 2024
# Day 4: Ceres Search
# find occurrences of xmas in a matrix

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

# diagonal extraction was written with help from chatgpt
# following prompt was used: search diagonally in a 2d array for strings in python
for i in range(len(crossword)):
    diagonal = []
    row, col = i, 0
    while row < len(crossword) and col < len(crossword):
        diagonal.append(crossword[row][col])
        row += 1
        col += 1
    str_row = ''.join(diagonal)
    xmas_count += str_row.count('XMAS') + str_row.count('SAMX')

    diagonal = []
    row, col = i, len(crossword[0])-1
    while row < len(crossword) and col >= 0:
        diagonal.append(crossword[row][col])
        row += 1
        col -= 1
    str_row = ''.join(diagonal)
    xmas_count += str_row.count('XMAS') + str_row.count('SAMX')


for i in range(1, len(crossword[0])):
    diagonal = []
    row, col = 0, i
    while row < len(crossword) and col < len(crossword):
        diagonal.append(crossword[row][col])
        row += 1
        col += 1
    str_row = ''.join(diagonal)
    xmas_count += str_row.count('XMAS') + str_row.count('SAMX')

    diagonal = []
    row, col = 0, i-1
    while row < len(crossword) and col >= 0:
        diagonal.append(crossword[row][col])
        row += 1
        col -= 1
    str_row = ''.join(diagonal)
    xmas_count += str_row.count('XMAS') + str_row.count('SAMX')

print(xmas_count)


# part 2

# lesson learned... don't use image processing techniques in a janky way

cross_count = 0

for i in range(len(crossword)-2):
    for j in range(len(crossword[0])-2):
        # get window rows
        window = crossword[i:i +3]
        # get window columns
        for x in range(len(window)):
            row = window[x]
            window[x] = row[j:j+3]

        if ''.join([window[0][0], window[1][1], window[2][2]]) in 'MAS SAM' and ''.join([window[0][2], window[1][1], window[2][0]]) in 'MAS SAM':
            cross_count += 1

print(cross_count)
