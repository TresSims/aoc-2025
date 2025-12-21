from functools import reduce

with open("/home/tsims/Documents/aoc-2025/inputs/day6.txt") as f:
    data = f.read().strip()

problems_array = [list(i) for i in data.split("\n")]
for row in problems_array:
    print(row)

height = len(problems_array)
width = len(problems_array[0])

problem = []
results = []

for row in reversed(range(width)):
    number = ""
    for col in range(height):
        try:
            new_item = problems_array[col][row]
            match new_item:
                case "*":
                    problem.append(number)
                    number = ""
                    solution = reduce(lambda x, y: int(x) * int(y), problem)
                    print("*".join(problem) + f" = {solution}")
                    results.append(solution)
                    problem = []
                case "+":
                    problem.append(number)
                    number = ""
                    solution = reduce(lambda x, y: int(x) + int(y), problem)
                    print("+".join(problem) + f" = {solution}")
                    results.append(solution)
                    problem = []
                case " ":
                    continue
                case _:
                    number += new_item
        except IndexError:
            continue

    if number.strip() != "":
        problem.append(number)

print(reduce(lambda x, y: x + y, results))
