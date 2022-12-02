from helper import *

# readString or readNumbers
data = readStrings("./days/day_2/example.txt")
# data = readStrings("./days/day_2/problem.txt")

def part1(data):
    sum = 0
    for i, point in enumerate(data):
        outcomes = point.split(" ")
        if outcomes[1] == 'X':
            sum += 1
            if outcomes[0] == 'A':
                sum += 3
            if outcomes[0] == 'C':
                sum += 6
        elif outcomes[1] == 'Y':
            sum += 2
            if outcomes[0] == 'B':
                sum += 3
            if outcomes[0] == 'A':
                sum += 6
        elif outcomes[1] == 'Z':
            sum += 3
            if outcomes[0] == 'C':
                sum += 3
            if outcomes[0] == 'B':
                sum += 6
    return sum


def part2(data):
    sum = 0
    for i, point in enumerate(data):
        outcomes = point.split(" ")
        if outcomes[1] == 'X':
            if outcomes[0] == 'A':
                sum += 3
            if outcomes[0] == 'B':
                sum += 1
            if outcomes[0] == 'C':
                sum += 2
        elif outcomes[1] == 'Y':
            sum += 3
            if outcomes[0] == 'A':
                sum += 1
            if outcomes[0] == 'B':
                sum += 2
            if outcomes[0] == 'C':
                sum += 3
        elif outcomes[1] == 'Z':
            sum += 6
            if outcomes[0] == 'A':
                sum += 2
            if outcomes[0] == 'B':
                sum += 3
            if outcomes[0] == 'C':
                sum += 1
    return sum


print(part1(data), part2(data))