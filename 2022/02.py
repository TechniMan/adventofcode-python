def get_data(filename: str) -> list[str]:
    with open(filename) as file:
        return [line for line in list(file)]


# R, P, S
opponents = ["A", "B", "C"]
mes_draw = ["X", "Y", "Z"]
mes_win = ["Y", "Z", "X"]
mes_lose = ["Z", "X", "Y"]

mes_result = ["X", "Y", "Z"]


def get_score_1(opponent: str, me: str) -> int:
    score = 0
    # points for the option you chose
    score += mes_draw.index(me) + 1
    # points for draw
    score += (3 * (mes_draw.index(me) == opponents.index(opponent)))
    # points for win
    score += (6 * (mes_win.index(me) == opponents.index(opponent)))
    # points for lose
    # score += (0 * (mes_lose.index(me) == opponents.index(opponent)))
    return score


def solve_part1(input: list[str]) -> int:
    total_score = 0
    for line in input:
        [o, m] = line.replace("\n", "").split(" ")
        total_score += get_score_1(o, m)
    return total_score


def get_score_2(opponent: str, me: str) -> int:
    score = 0
    # points for outcome
    score += 3 * mes_result.index(me)

    me_selection = 0
    # what do I use to lose
    if me == "X":
        opponent_selection = opponents.index(opponent)
        me_selection = mes_lose[opponent_selection]
    # what do I use to draw
    elif me == "Y":
        opponent_selection = opponents.index(opponent)
        me_selection = mes_draw[opponent_selection]
    # what do I use to win
    else:
        opponent_selection = opponents.index(opponent)
        me_selection = mes_win[opponent_selection]
    # add points for my selection
    score += 1 + mes_draw.index(me_selection)
    return score


def solve_part2(input: list[str]) -> int:
    total_score = 0
    for line in input:
        [o, m] = line.replace("\n", "").split(" ")
        total_score += get_score_2(o, m)
    return total_score


input = get_data("02.txt")
print(str(solve_part1(input)))
print(str(solve_part2(input)))
