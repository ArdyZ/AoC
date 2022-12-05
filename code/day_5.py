from helper import *

# readString or readNumbers
data_example = readStrings("./days/day_5/example.txt")
data = readStrings("./days/day_5/problem.txt")

def getStacksOperations(data):
    crates = True
    stacks = [[], [], [], [], [], [], [], [], []]
    operations = []
    for line in data:
        if line == '':
            crates = False
            continue
        if crates:
            for i in range(0, 4*9, 4):
                if line[i+1:i+2] == ' ':
                    continue
                if line[i+1:i+2] == '1':
                    break
                stacks[int(i/4)] = [line[i+1:i+2]] + stacks[int(i/4)]
        else:
            amount, line = line.split("move ")[1].split(" from ")
            orgin, to = line.split(" to ")
            operations.append([int(amount), int(orgin), int(to)])
    return operations, stacks

def part1(data):
    operations, stacks = getStacksOperations(data)
    for operation in operations:
        for i in range(operation[0]):
            item = stacks[operation[1]-1].pop()
            stacks[operation[2]-1].append(item)
    
    line = ""
    for i in stacks:
        line += i.pop()
    return line


def part2(data):
    operations, stacks = getStacksOperations(data)

    for operation in operations:
        item = []
        for i in range(operation[0]):
            item = [stacks[operation[1]-1].pop()] + item
        stacks[operation[2]-1] += item
    
    line = ""
    for i in stacks:
        line += i.pop()
    return line

print(part1(data_example), part2(data_example))
print(part1(data), part2(data))