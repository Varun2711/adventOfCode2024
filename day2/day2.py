# Advent of code 2024
# Day 2
# Find safe reports


# list of reports: 2d matrix
# report: a row in the matrix
# a report is safe if row is all increasing or all decreasing
# and adjacent levels differ by at least one and not more than 3

safe_count = 0
reports = []

# process input and generate matrix
with open('input.txt', 'r') as f:
    for line in f.readlines():
        report = [int(x) for x in line.split()]
        reports.append(report)

# process data and generate safe count
for report in reports:
    
    # check increase or decreasing:
    increasing = all(j - i > 0 and 1 <= abs(i - j) <= 3 for i, j in zip(report, report[1::]))
    decreasing = all(j - i < 0 and 1 <= abs(i -j) <= 3 for i ,j in zip(report, report[1::]))

    if increasing or decreasing:
        safe_count += 1

print(safe_count)
    