from helper import *

# readString or readNumbers
data_example = readStrings("./days/day_6/example.txt")
data = readStrings("./days/day_6/problem.txt")


def part(data, amount):
    results = []
    for line in data:
        previous = []
        for i, char in enumerate(line):
            if len(previous) < amount-1:
                if char in previous:
                    while previous.pop(0) != char:
                        continue
                previous.append(char)
            elif len(previous) < amount:
                if char in previous:
                    while previous.pop(0) != char:
                        continue
                    previous.append(char)
                else:
                    results.append(i + 1)
                    break
            else:
                if char in previous:
                    while previous.pop(0) != char:
                        continue
                    previous.append(char)
                else:
                    results.append(i + 1)
                    break
    return results

print(part(data_example, 4), part(data_example, 14))
print(part(data, 4), part(data, 14))