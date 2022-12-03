from helper import *

# readString or readNumbers
data_example = readStrings("./days/day_3/example.txt")
# data = readStrings("./days/day_3/problem.txt")

def part1(data):
    sum = 0

    for i, point in enumerate(data):
        for j in range(int(len(point)/2)):
            if point[int(len(point)/2):].__contains__(point[:int(len(point)/2)][j]):
                test = point[:int(len(point)/2)][j]
                if test.lower() == test:
                    sum +=  ord(test) - 96
                else:
                    sum += ord(test) - 64 + 26
                break
    return sum


def part2(data):
    sum = []
    result = 0
    
    for i, point in enumerate(data):
        if i % 3 == 0:
            for j in range(len(sum)):
                if len(sum[j]) == 3:
                    result += j

            sum = []
            for j in range (53):
                sum.append([])
        for j in range(len(point)):
            test = point[j]
            temp = 0
            if test.lower() == test:
                temp +=  ord(test) - 96
            else:
                temp += ord(test) - 64 + 26
            if not i in sum[temp]:
                sum[temp].append(i)

    for j in range(len(sum)):
        if len(sum[j]) == 3:
            result += j
    return result

print(part1(data_example), part2(data_example))
print(part1(data), part2(data))