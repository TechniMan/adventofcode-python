import time


def get_data() -> list[str]:
    return [line for line in open("10.txt").read().split("\n")]


def signal_strength(clock: int, val: int) -> int:
    if clock == 20 or clock == 60 or clock == 100 or clock == 140 or clock == 180 or clock == 220:
        print(f"{clock} * {val} => {clock * val}")
        return clock * val
    return 0


# current_row: int = 0
# crt_display = ["", "", "", "", "", ""]  # 6 rows


def print_pixel(clock: int, x: int) -> None:
    global crt_display, current_row
    crt = clock % 40
    if crt == x - 1 or crt == x or crt == x + 1:
        print("#", end="", flush=True)
        # crt_display[current_row] += "#"
    else:
        print(" ", end="", flush=True)
        # crt_display[current_row] += "."
    # print(f"{clock}: c{crt} x{x} => {crt_display[current_row][len(crt_display[current_row]) - 1]}")

    if crt == 0:
        print("*", flush=True)
        # current_row += 1
    time.sleep(0.00625)


def solve_part1(input: list[str]) -> int:
    clock = 0
    X = 1
    result = 0
    for line in input:
        parts = line.split(" ")
        instruction = parts[0].strip()
        if instruction == "noop":
            clock += 1
            result += signal_strength(clock, X)
        elif instruction == "addx":
            # cycle 1
            clock += 1
            result += signal_strength(clock, X)
            # cycle 2
            clock += 1
            result += signal_strength(clock, X)
            X += int(parts[1].strip())
    return result


def solve_part2(input: list[str]) -> None:
    clock = 0
    X = 1
    for line in input:
        parts = line.split(" ")
        instruction = parts[0].strip()
        # cycle 1
        clock += 1
        print_pixel(clock, X)
        # cycle 2
        if instruction == "addx":
            clock += 1
            X += int(parts[1].strip())
            print_pixel(clock, X)

    # for row in crt_display:
    #     print(row)


input = get_data()
print(str(solve_part1(input)))
print()
solve_part2(input)
