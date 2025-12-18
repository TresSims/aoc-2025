with open("/home/tsims/Documents/aoc-2025/inputs/day5.txt") as f:
    input_file = f.read()

lines = input_file.split("\n")
split = lines.index("")
fresh = lines[:split]
ingredients = [int(i) for i in lines[split + 1 : -1]]
fresh_count = 0
# for ingredient in ingredients:
#     for entry in fresh:
#         entries = [int(i) for i in entry.split("-")]
#         if ingredient >= entries[0] and ingredient <= entries[1]:
#             fresh_count += 1
#             break

codes = set()
waitForInput = 0
maxWait = 10000000
for fresh_range in fresh:
    entries = [int(i) for i in fresh_range.split("-")]
    for i in range(entries[0], entries[1] + 1):
        codes.add(i)
        waitForInput += 1
        if waitForInput > maxWait:
            input("Waiting for input")
            waitForInput = 0


print(f"Day 5 - {len(codes)}")
