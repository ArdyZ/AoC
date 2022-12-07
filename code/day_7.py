from helper import *

# readString or readNumbers
data_example = readStrings("./days/day_7/example.txt")
data = readStrings("./days/day_7/problem.txt")


def calc(dic_result, key):
    result = 0
    for item in dic_result[key]:
        if item.isnumeric():
            result += int(item)
        else:
            result += calc(dic_result, key + item)
    return result


def parse(data):
    current_dir = []
    dic_result = {}
    for i, line in enumerate(data):
        line = line.split(" ");
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    current_dir = ["/"]
                elif line[2] == "..":
                    current_dir.pop()
                else:
                    current_dir.append(line[2])
            else:
                continue
        else:
            if not ''.join(current_dir) in dic_result.keys():
                dic_result[''.join(current_dir)] = []
            if line[0] == "dir":
                dic_result[''.join(current_dir)] = dic_result[''.join(current_dir)] + [line[1]]
            else:
                dic_result[''.join(current_dir)] = dic_result[''.join(current_dir)] + [line[0]]
    return dic_result


def part1(data):
    dic_result = parse(data)
    
    res = 0
    for key in dic_result.keys():
        temp = calc(dic_result, key)
        if temp <= 100000:
            res += temp
    return res


def part2(data):
    dic_result = parse(data)
        
    dic_sizes = {}
    for key in dic_result.keys():
        temp = calc(dic_result, key)
        dic_sizes[key] = temp

    current_space = 30000000 - (70000000 - dic_sizes["/"])
    current_size = dic_sizes["/"]
    for key in dic_sizes.keys():
        if dic_sizes[key] >= current_space and dic_sizes[key] <= current_size:
            current_size = dic_sizes[key]
    return current_size

print(part1(data_example), part2(data_example))
print(part1(data), part2(data))