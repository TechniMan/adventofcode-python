def get_data(filename: str) -> list[str]:
    with open(filename) as file:
        return [line for line in list(file)]


priorities = ['@', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def get_priority(type: chr) -> int:
    # ordinal = ord(type) - ord('A') + 1
    # if type.isupper():
    #     ordinal += 26
    # else:
    #     ordinal -= 32
    # return ordinal
    return priorities.index(type)


def solve_part1(rucksacks: list[str]) -> int:
    sum_priority = 0
    for rucksack in rucksacks:
        # split into compartments (halves)
        half_len = int(len(rucksack) / 2)
        compA = rucksack.strip()[0:half_len]
        compB = rucksack.strip()[half_len:]
        # find char that matches
        matching_char = 'A'
        for cA in compA:
            for cB in compB:
                if cA == cB:
                    matching_char = cA
                    break
        # add priority to sum_priority
        priority = get_priority(matching_char)
        sum_priority += priority
        # print(str(matching_char) + " " + str(priority))
    return sum_priority


def solve_part2(rucksacks: list[str]) -> int:
    sum_priority = 0
    # loop three at a time
    r = 0
    while r < len(rucksacks):
        ruck1 = rucksacks[r].strip()
        ruck2 = rucksacks[r + 1].strip()
        ruck3 = rucksacks[r + 2].strip()
        badge = 'a'
        for r1 in ruck1:
            for r2 in ruck2:
                for r3 in ruck3:
                    if r1 == r2 and r1 == r3:
                        badge = r1
                        break
        sum_priority += get_priority(badge)
        r += 3
    return sum_priority


rucksacks = get_data("03.txt")
print(solve_part1(rucksacks))
print(solve_part2(rucksacks))

# for i in range(ord('A'), ord('z')):
#     print(str(chr(i)) + " - " + str(i))
