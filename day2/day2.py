# Advent of code 2024
# Day 2
# Find safe reports


# list of reports: 2d matrix
# report: a row in the matrix
# a report is safe if row is all increasing or all decreasing
# and adjacent levels differ by at least one and not more than 3

reports = []

# process input and generate matrix
with open('../inputs/day2input.txt', 'r') as f:
    for line in f.readlines():
        report = [int(x) for x in line.split()]
        reports.append(report)

# process data and generate safe count and create unsafe report matrix
unsafe_reports = []
def generate_safe_count(reports):
    safe_count = 0
    for report in reports:
        
        # check increase or decreasing:
        increasing = all(j - i > 0 and 1 <= abs(i - j) <= 3 for i, j in zip(report, report[1::]))
        decreasing = all(j - i < 0 and 1 <= abs(i -j) <= 3 for i ,j in zip(report, report[1::]))

        if increasing or decreasing:
            safe_count += 1
        else:
            unsafe_reports.append(report)
    return safe_count

generate_safe_count(reports=reports)
print(len(reports), len(unsafe_reports))

# got stuck on part 2
# soln from u/Independent_Check_62 from r/adventofcode
def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

safe_count = sum([any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))for report in reports])


print(safe_count)
        