def get_data(filename: str) -> list[str]:
    with open(filename) as file:
        return [line for line in list(file)]


# start_state is a list of stacks of the crates' letters
# each instruction is a string formatted thus: "quantity,origin,destination"
def solve_part1(start_state: list[list[chr]], instructions: list[str]) -> str:
    state: list[list[chr]] = start_state
    # follow instructions
    for instruction in instructions:
        [quantity, origin, destination] = instruction.split(',')
        for i in range(int(quantity)):
            # pop off of origin stack and append onto destination stack
            state[int(destination)].append(state[int(origin)].pop())
    # determine top crate of each stack
    top_row = ""
    for stack in state:
        top_row = top_row + stack.pop()
    return top_row


input = get_data("05.txt")
start_state_lines: list[str] = []
instructions_lines: list[str] = []

# 0 = start_state_lines; 1 = instructions_lines
state: int = 0
for line in input:
    if state == 0:
        if line == "\n":
            state = 1
        else:
            # don't strip; retain the whitespace!
            start_state_lines.append(line)
    else:
        instructions_lines.append(line.strip())

# STACK INTERPRETATION
# list of lists of strings
start_state: list[list[chr]] = []
# cheat; there are 9 stacks in the input
stack_count: int = 9

# initialise the initial stacks
for s in range(stack_count):
    start_state.append([])

# interpret the stack info
for line in start_state_lines:
    for stack in range(stack_count):
        sIdx: int = 1 + stack * 4
        if line[sIdx] != ' ':
            start_state[stack].append(line[sIdx])

# pop off the number and reverse for lifo
for s in range(stack_count):
    start_state[s].pop()
    start_state[s].reverse()
    # print(start_state[s])

# INSTRUCTIONS INTERPRETATION
# quantity,origin,destination
instructions: list[str] = []
# read from the string to get the info we want
for line in instructions_lines:
    parts = line.split(' ')
    # change range of stack IDs from 1-9 to 0-8 for easy indexing
    instruction = parts[1] + "," + str(int(parts[3]) - 1) + "," + str(int(parts[5]) - 1)
    instructions.append(instruction)
    # print(instruction)

print(solve_part1(start_state, instructions))
