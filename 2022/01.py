def get_data(filename: str) -> list[str]:
    with open(filename) as file:
        return [line for line in list(file)]


def count_calories(input: list[str]) -> list[int]:
    elves = []
    current_elf = 0
    for food in input:
        if food == "\n":
            elves.append(current_elf)
            current_elf = 0
        else:
            current_elf += int(food.strip())
    return elves


def solve_part1(elves: list[int]) -> int:
    highest = 0
    for elf in elves:
        if elf > highest:
            highest = elf
    return highest


def solve_part2(elves: list[int]) -> int:
    elves.sort()
    elves.reverse()
    return elves[0] + elves[1] + elves[2]


input = get_data("01.txt")
elves = count_calories(input)
print("Part 2: " + str(solve_part1(elves)))
print("Part 1: " + str(solve_part2(elves)))
