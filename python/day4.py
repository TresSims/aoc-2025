import numpy as np

image = []
roll = "@"
targets = 0
max_n = 4
r = 1


def remove_rolls(image) -> tuple[int, np.ndarray]:
    n_targets = 0
    for x in range(0, len(image)):
        for y in range(0, len(image[x])):
            if image[x][y] == 1:
                min_x = max(x - r, 0)
                max_x = min(x + r + 1, len(image))
                min_y = max(y - r, 0)
                max_y = min(y + r + 1, len(image[x]))
                sub_arr = image[min_x:max_x, min_y:max_y]
                neigh = np.sum(sub_arr) - 1
                if neigh < max_n:
                    print(sub_arr)
                    n_targets += 1
                    image[x][y] = 0

    return n_targets, image


with open("/home/tsims/Documents/aoc-2025/inputs/day4.txt") as f:
    for line in f.readlines():
        new_line = []
        for i in line.strip():
            new_line.append(1 if i == roll else 0)
        image.append(new_line)


image = np.array(image)
while True:
    n, image = remove_rolls(image)
    targets += n
    if n == 0:
        break

print(f"Day 2 - {targets}")
