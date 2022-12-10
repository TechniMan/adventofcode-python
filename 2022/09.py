# classes
class Vector:
    def __init__(self, x: int = 0, y: int = 0):
        self.x: int = x
        self.y: int = y

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def __str__(self) -> str:
        return "{" + str(self.x) + "," + str(self.y) + "}"


# functions
def get_data() -> list[str]:
    return [line for line in open("09.txt").read().split("\n")]


# count number of tiles between two co-ordinates
def distance(a: Vector, b: Vector) -> int:
    xDiff = b.x - a.x
    yDiff = b.y - a.y
    return max(abs(xDiff), abs(yDiff))


def difference(a: Vector, b: Vector) -> Vector:
    xDiff = b.x - a.x
    yDiff = b.y - a.y
    return Vector(xDiff, yDiff)


def solve_part1(input: list[str]) -> int:
    # init
    tiles_touched = set()
    head_x = 0
    head_y = 0
    tail_x = 0
    tail_y = 0
    tiles_touched.add("{0,0}")
    for line in input:
        # interpret direction and movement
        direction = line[0]
        movement = int(line[2:])
        # print(f"{line}")
        # perform each movement step
        for _ in range(movement):
            # first, move the head
            if direction == "U":
                head_y -= 1
            elif direction == "D":
                head_y += 1
            elif direction == "L":
                head_x -= 1
            elif direction == "R":
                head_x += 1
            else:
                print(f"Can't move in direction {direction}! From line: {line}")
                exit()
            # then, move the tail if the head is far enough away
            distance = max(abs(head_x - tail_x), abs(head_y - tail_y))
            x_diff = head_x - tail_x
            y_diff = head_y - tail_y
            if distance > 1:
                # find the appropriate direction to move the tail toward the head
                if x_diff == 2:
                    tail_x += 1
                    if y_diff == 1:
                        tail_y += 1
                    elif y_diff == -1:
                        tail_y -= 1
                elif x_diff == -2:
                    tail_x -= 1
                    if y_diff == 1:
                        tail_y += 1
                    elif y_diff == -1:
                        tail_y -= 1
                elif y_diff == 2:
                    tail_y += 1
                    if x_diff == 1:
                        tail_x += 1
                    elif x_diff == -1:
                        tail_x -= 1
                elif y_diff == -2:
                    tail_y -= 1
                    if x_diff == 1:
                        tail_x += 1
                    elif x_diff == -1:
                        tail_x -= 1
                # only add to the list if not already present
                key = f"{{{tail_x},{tail_y}}}"
                tiles_touched.add(key)
            if distance > 2:
                print("Distance is greater than two!")
    return len(tiles_touched)


# setup
input = get_data()
print(str(solve_part1(input)))
