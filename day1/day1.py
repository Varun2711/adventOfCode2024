# Advent of code 2024
# Day 1
# Find total distance


# Part one
left = []
right = []

with open('../inputs/day1input.txt', 'r') as f:
    for line in f.readlines():
        l, r = line.split()

        left.append(int(l))
        right.append(int(r))


left.sort()
right.sort()

total_distance = sum([abs(x-y) for x, y in zip(left, right)])

print(total_distance)


# part 2

counts = {}

for n in left:
    counts[n] = 0

for n in right:
    if n in counts:
        counts[n] += 1
    

s = 0
for key, val in counts.items():
    s += (key * val)

print(s)



