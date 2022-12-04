from helper import *

# readString or readNumbers
data_example = readStrings("./days/day_4/example.txt")
data = readStrings("./days/day_4/problem.txt")

def part1(data):
    sum = 0
    for i, item in enumerate(data):
        item = item.split(",")
        l1 = int(item[0].split("-")[0])
        l2 = int(item[0].split("-")[1])
        r1 = int(item[1].split("-")[0])
        r2 = int(item[1].split("-")[1])

        if l1 <= r1 and l2 >= r2:
            sum += 1
        elif r1 <= l1 and r2 >= l2:
            sum += 1
    return sum


def part2(data):
    sum = 0
    for i, item in enumerate(data):
        item = item.split(",")
        l1 = int(item[0].split("-")[0])
        l2 = int(item[0].split("-")[1])
        r1 = int(item[1].split("-")[0])
        r2 = int(item[1].split("-")[1])

        if l1 <= r1 and l2 >= r2:
            sum += 1
        elif r1 <= l1 and r2 >= l2:
            sum += 1
        elif l1 <= r1 and l2 >= r1:
            sum += 1
        elif l1 <= r2 and l1 >= r1:
            sum += 1
        elif r1 <= l1 and r2 >= l1:
            sum += 1
        elif r1 <= l2 and r1 >= l1:
            sum += 1
    return sum

print(part1(data_example), part2(data_example))
print(part1(data), part2(data))