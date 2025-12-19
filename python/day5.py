class DataRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getSize(self):
        return self.end - self.start + 1

    def __repr__(self):
        return f"[{self.start:,}, {self.end:,}]"


dataRanges = []

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

for fresh_range in fresh:
    entries = [int(i) for i in fresh_range.split("-")]
    dataRanges.append(DataRange(entries[0], entries[1]))

dataRanges.sort(key=lambda data: data.start)

extraLookback = 1
i = 1
while i < len(dataRanges):
    if dataRanges[i].start <= dataRanges[i - 1].end:
        dataRanges[i].start = dataRanges[i - 1].end + 1

    if dataRanges[i].start > dataRanges[i].end:
        dataRanges.pop(i)
        continue

    i += 1

for data in dataRanges:
    fresh_count += data.getSize()

print(dataRanges)
print(f"Day 5 - {fresh_count}")
