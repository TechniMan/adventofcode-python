# functions
def get_data() -> list[str]:
    with open("08.txt") as file:
        return [line.strip() for line in list(file)]


def lines_to_grid(lines: list[str]) -> list[int]:
    grid: list[int] = []
    for line in lines:
        for char in line:
            grid.append(int(char))
    return grid


def solve_part1(tree_grid: list[int], grid_width: int) -> int:
    # start with all edge trees counted
    visible_trees = (grid_width * 4) - 4
    # for each tree (i.e. each cell in grid, excluding borders)
    for y in range(1, grid_width - 1):
        for x in range(1, grid_width - 1):
            idx = x + (y * grid_width)
            h = tree_grid[idx]  # height of tree to scan
            # scan each direction away from the tree; as soon as vision blocked, move on to next
            tree_visible_n = True
            for v in range(y - 1, -1, -1):
                # if our tree is blocked by this tree:
                if tree_grid[x + (v * grid_width)] >= h:
                    tree_visible_n = False
                    break
            # scan east of the tree
            tree_visible_e = True
            for u in range(x - 1, -1, -1):
                # if our tree is blocked by this tree:
                if tree_grid[u + (y * grid_width)] >= h:
                    tree_visible_e = False
                    break
            # scan south of the tree
            tree_visible_s = True
            for v in range(y + 1, grid_width, 1):
                # if our tree is blocked by this tree:
                if tree_grid[x + (v * grid_width)] >= h:
                    tree_visible_s = False
                    break
            # scan west of the tree
            tree_visible_w = True
            for u in range(x + 1, grid_width, 1):
                # if our tree is blocked by this tree:
                if tree_grid[u + (y * grid_width)] >= h:
                    tree_visible_w = False
                    break
            if tree_visible_n or tree_visible_e or tree_visible_s or tree_visible_w:
                visible_trees += 1
    return visible_trees


def solve_part2(tree_grid: list[int], grid_width: int) -> int:
    # all edge trees have a 0 on at least one side, so score is 0 for those
    highest_scenic_score = 0
    # for each tree (i.e. each cell in grid, excluding borders)
    for y in range(1, grid_width - 1):
        for x in range(1, grid_width - 1):
            idx = x + (y * grid_width)
            h = tree_grid[idx]  # height of tree to scan
            # scan north of the tree
            trees_visible_n = 0
            for v in range(y - 1, -1, -1):
                # if our tree is blocked by this tree:
                if tree_grid[x + (v * grid_width)] >= h or v == 0:
                    trees_visible_n = y - v
                    break
            # scan east of the tree
            trees_visible_e = 0
            for u in range(x - 1, -1, -1):
                # if our tree is blocked by this tree:
                if tree_grid[u + (y * grid_width)] >= h or u == 0:
                    trees_visible_e = x - u
                    break
            # scan south of the tree
            trees_visible_s = 0
            for v in range(y + 1, grid_width, 1):
                # if our tree is blocked by this tree:
                if tree_grid[x + (v * grid_width)] >= h or v == (grid_width - 1):
                    trees_visible_s = v - y
                    break
            # scan west of the tree
            trees_visible_w = 0
            for u in range(x + 1, grid_width, 1):
                # if our tree is blocked by this tree:
                if tree_grid[u + (y * grid_width)] >= h or u == (grid_width - 1):
                    trees_visible_w = u - x
                    break
            score = trees_visible_n * trees_visible_e * trees_visible_s * trees_visible_w
            if score > highest_scenic_score:
                print(f"x:{x}, y:{y}, n:{trees_visible_n}, e:{trees_visible_e}, s:{trees_visible_s}, w:{trees_visible_w}, score:{score}")
                highest_scenic_score = int(score)
    return highest_scenic_score


# setup
input = get_data()
trees = lines_to_grid(input)
print(str(solve_part1(trees, len(input[0]))))
print(str(solve_part2(trees, len(input[0]))))
