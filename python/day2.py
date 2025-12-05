with open("/home/tsims/Documents/aoc-2025/inputs/day2.txt") as f:
    content = f.read()
    ranges = content.split(",")
    count = 0
    invalid = []
    for rang in ranges:
        print(f"Range {rang}")
        vals = rang.split("-")
        for num in range(int(vals[0]), int(vals[1]) + 1):
            string_num = str(num)
            num_len = len(string_num)
            for p in range(2, num_len + 1):
                if num_len % p == 0:
                    segments = []
                    segment_length = num_len // p
                    a = string_num[0 : num_len // 2]
                    b = string_num[num_len // 2 :]
                    for q in range(0, p):
                        segments.append(
                            string_num[q * segment_length : (q + 1) * segment_length]
                        )
                    if len(set(segments)) == 1:
                        invalid.append(num)
                        print(f"adding {string_num}")

print(f"Day 2: {sum(set(invalid))}")
