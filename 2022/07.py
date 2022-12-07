# classes
class Directory:
    def __init__(self, name: str, parent=None):
        self.name: str = name
        self.size: int = 0
        self.children: list[Directory] = []
        self.parent = parent

    def __str__(self) -> str:
        return f"{self.name.ljust(19)} : {str(self.size).rjust(8)}"

    def add_file(self, name: str, size: int) -> None:
        # travel path to add size to
        self.size += size

    def add_child(self, child) -> None:
        # travel path to add dir to
        self.children.append(child)

    def get_total_size(self) -> int:
        total = 0 + self.size
        for child in self.children:
            total += child.get_total_size()
        return total


# functions
def get_data() -> list[str]:
    with open("07.txt") as file:
        return [line for line in list(file)]


# read commands and output and build a dictionary/map of dir paths and total sizes
def interpret_terminal_out_dict(input: list[str]) -> dict[str, int]:
    root: dict[str, int] = {"/": 0}
    cwd: str = "/"
    for line in input:
        if line[0] == '$':
            # alter cwd as appropriate; either adding or removing a section
            if line[2:4] == "cd":
                dir: str = line[5:-1]
                if dir == "..":
                    # go up a level by slicing cwd
                    cwd = cwd[:cwd[:cwd.rfind("/")].rfind("/") + 1]
                elif dir == "/":
                    # go straight to root
                    cwd = "/"
                else:
                    # go down a level by adding to cwd
                    cwd += dir + "/"
        elif line[0:3] == "dir":
            # describes directory: add new key to dictionary
            dir: str = line.split(' ')[1].strip()
            path: str = cwd + dir + "/"
            root[path] = 0
        else:
            # describes file: add size to cwd
            size: int = int(line.split(' ')[0])
            root[cwd] += size
            # also add size to parent directories all the way up the hierarchy
            parents: list[str] = []
            parts: list[str] = cwd.split('/')[1:]
            parent: str = "/"
            for part in parts:
                print(f"{cwd}: {parent}")
                root[parent] += size
                parent += part + "/"
    return root


# read commands and output and build a dictionary/map of dir paths and total sizes
def interpret_terminal_out_directory(input: list[str]) -> Directory:
    root: Directory = Directory("/")
    cwd: Directory = root
    for line in input:
        if line[0] == '$':
            # go to appropriate directory to continue
            if line[2:4] == "cd":
                dir: str = line[5:-1]  # -1 to discard the newline
                if dir == "..":
                    # go up a level
                    cwd = cwd.parent
                elif dir == "/":
                    # go straight to root
                    cwd = root
                else:
                    # go down a level
                    for child in cwd.children:
                        if child.name == dir:
                            cwd = child
                            break
        elif line[0:3] == "dir":
            # describes directory: add new directory
            dir = Directory(line.split(' ')[1].strip(), cwd)
            cwd.add_child(dir)
        else:
            # describes file: add size to cwd
            parts = line.split(' ')
            cwd.add_file(parts[1], int(parts[0]))
    return root


dirs_smaller_than: list[Directory] = []


# recursive; adds to list above
def find_dirs_smaller_than(size_limit: int, dir: Directory) -> None:
    # do this dir
    if dir.get_total_size() <= size_limit:
        dirs_smaller_than.append(dir)

    # now do its children
    for child in dir.children:
        find_dirs_smaller_than(size_limit, child)


dirs_larger_than: list[Directory] = []


# recursive; adds to list above
def find_dirs_larger_than(size_limit: int, dir: Directory) -> None:
    # do this dir
    if dir.get_total_size() >= size_limit:
        dirs_larger_than.append(dir)

    # now do its children
    for child in dir.children:
        find_dirs_larger_than(size_limit, child)


# solutions
def solve_part1(root: Directory) -> int:
    total = 0
    # dict solution
    # for dir in fs:
    #     print(f"{dir}: {fs[dir]}")
    #     if fs[dir] <= 100000:
    #         print("Added")
    #         total += fs[dir]
    # Directory solution
    find_dirs_smaller_than(100000, root)
    for d in dirs_smaller_than:
        total += d.get_total_size()
    return total


def solve_part2(root: Directory) -> int:
    size_required = 70000000 - root.get_total_size()
    find_dirs_larger_than(size_required, root)
    smallest: int = 70000000
    for d in dirs_larger_than:
        if d.get_total_size() < smallest:
            smallest = d.get_total_size()
    return smallest


# setup
input = get_data()
# root_fs_dict: dict[str, int] = interpret_terminal_out_dict(input)
root_fs_directory: Directory = interpret_terminal_out_directory(input)
# print(root_fs)
# add up all subfolders of every folder
print(str(solve_part1(root_fs_directory)))
print(str(solve_part2(root_fs_directory)))
