def read_stream() -> str:
    return open("06.txt").readline()


def is_unique(s: str) -> bool:
    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                continue
            elif s[i] == s[j]:
                return False
    return True


# returns index of the start-of-packet marker
def find_start_of_packet_marker(buf: str) -> int:
    i = 3
    while True:
        slice = buf[i-3:i+1]
        if is_unique(slice):
            break
        i += 1
    return i + 1


def solve_part1() -> int:
    return find_start_of_packet_marker(read_stream())


# returns index of the start-of-message marker
def find_start_of_message_marker(buf: str) -> int:
    i = 13
    while True:
        slice = buf[i-13:i+1]
        if is_unique(slice):
            break
        i += 1
    return i + 1


def solve_part2() -> int:
    return find_start_of_message_marker(read_stream())


print(str(solve_part1()))
print(str(solve_part2()))
