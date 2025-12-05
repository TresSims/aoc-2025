with open("/home/tsims/Documents/aoc-2025/inputs/day3.txt") as f:
    bank_highs = []
    for line in f.readlines():
        digits_to_find = 12
        bank_digits = []
        i_line = [int(i) for i in line.strip()]
        while digits_to_find > 0:
            searchable_array = i_line[0 : len(i_line) - digits_to_find + 1]
            bank_digits.append(max(searchable_array))
            new_start = i_line.index(bank_digits[-1]) + 1
            i_line = i_line[new_start:]
            digits_to_find -= 1

        new_bank = "".join(map(str, bank_digits))
        # print(f"Max for {line} is {new_bank}")
        bank_highs.append(int(new_bank))

    # print(bank_highs)
    print(f"Day 2 - {sum(bank_highs)}")
