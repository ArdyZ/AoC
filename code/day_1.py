from helper import *

data = readStrings("./days/day_1/problem.txt")
# data = readStrings("./days/day_1/example.txt")

result = []
current_sum = 0 

for i in range(0, len(data)):
    if (data[i] == ''):
        result.append(current_sum)
        current_sum = 0 
    else:
        current_sum += int(data[i])

print('day1_1:', sorted(result)[-1])
print('day1_2:', sum([sorted(result)[-1], sorted(result)[-2], sorted(result)[-3]]))