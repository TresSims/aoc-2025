import numpy as np
from functools import reduce

with open("/home/tsims/Documents/aoc-2025/inputs/day6-min.txt") as f:
    data = f.read().strip()


rows = [x.split() for x in data.split("\n")]
problems = np.array(rows)
problems = problems.transpose()
print(problems)

results = []
for problem in problems:
    operation = problem[-1]

    match operation:
        case "*":
            results.append(reduce(lambda x, y: int(x) * int(y), problem[:-1]))
        case "+":
            results.append(reduce(lambda x, y: int(x) + int(y), problem[:-1]))
        case _:
            print("Shit's fucked")
            exit()

print(results)
print(reduce(lambda x, y: x + y, results))
