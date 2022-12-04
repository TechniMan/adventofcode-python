def get_data(filename: str) -> list[str]:
    with open(filename) as file:
        return [line for line in list(file)]


def solve_part2(input: list[str]) -> int:
    count_pairs = 0
    for pair in input:
        # figure out their assignments
        [elf_a, elf_b] = pair.strip().split(",")
        [a_start, a_end] = elf_a.split("-")
        [b_start, b_end] = elf_b.split("-")
        # find if there is any overlap
        if int(a_start) <= int(b_end) and int(a_end) >= int(b_start):
            # a is contained in b
            count_pairs += 1
        elif int(b_start) >= int(a_end) and int(b_end) <= int(a_start):
            # b is contained in a
            count_pairs += 1
    return count_pairs


def solve_part1(input: list[str]) -> int:
    count_pairs = 0
    for pair in input:
        # figure out their assignments
        [elf_a, elf_b] = pair.strip().split(",")
        [a_start, a_end] = elf_a.split("-")
        [b_start, b_end] = elf_b.split("-")
        # find if one is wholly encompassed by the other
        if int(a_start) >= int(b_start) and int(a_end) <= int(b_end):
            # a is contained in b
            count_pairs += 1
        elif int(b_start) >= int(a_start) and int(b_end) <= int(a_end):
            # b is contained in a
            count_pairs += 1
    return count_pairs


input = get_data("04.txt")
print(solve_part1(input))
print(solve_part2(input))
