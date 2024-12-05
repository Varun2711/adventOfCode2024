# Advent of code 2024
# Day 3
# process corrupted memory to computer sum of products

# part 1

# use regex to find all non corrupted entries
# then process the entries

import re

# get data
data = None

with open('../inputs/day3input.txt', 'r') as f:
    data = f.read()


pattern = 'mul\(\d+,\d+\)'

entries = re.findall(pattern, data)


sop = 0 # sum or products

for entry in entries:
    p2 = '[0-9]+'
    nums = [int(x) for x in re.findall(p2, entry)]
    sop += nums[0] * nums[1]

print(sop)

# part 2

dd_pattern = "(don't|do)"

dd = re.finditer(dd_pattern, data)

idx = 0
do = True
sop = 0
for next_item in dd:
    end = next_item.start()
    if do:
        window = data[idx:next_item.start()]
        pattern = 'mul\(\d+,\d+\)'

        entries = re.findall(pattern, window)

        for entry in entries:
            p2 = '[0-9]+'
            nums = [int(x) for x in re.findall(p2, entry)]
            sop += nums[0] * nums[1]
    idx = next_item.end()
    do = True if next_item.group()== 'do' else False

print(sop)


    