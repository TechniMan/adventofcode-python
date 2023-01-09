from time import time


# flags
verbose = False
part1 = True


# classes
class Monkey:
    '''
    items: list of items represented as worry level
    operation: function to call on an item when inspected by the monkey
    test: function to call on an item after inspected by monkey
    '''

    def __init__(
        self,
        starting_items: list[int],
        operator_is_add: str,
        operand: int,
        test_divisor: int,
        test_pass_target: int,
        test_fail_target: int
    ):
        self.items = starting_items
        self.operator_is_add = operator_is_add
        self.operand = operand
        self.test_divisor = test_divisor
        self.test_pass_target = test_pass_target
        self.test_fail_target = test_fail_target

        self.items_inspected = 0

    def operation(self, item: int) -> int:
        if verbose:
            print(f"  Monkey inspects an item with a worry level of {item}.")
        operand = self.operand
        if operand == 0:
            operand = item
        self.items_inspected += 1
        result = (item + operand) if self.operator_is_add else (item * operand)
        if verbose:
            print(f"    Worry level {'is multiplied' if self.operator_is_add else 'increases'} by {operand} to {result}.")
        return result

    def test(self, item: int) -> int:
        # a if condition else b
        if (item % self.test_divisor) == 0:
            if verbose:
                print(f"    Current worry level is divisible by {self.test_divisor}.")
                print(f"    Item with worry level {item} is thrown to monkey {self.test_pass_target}.")
            return self.test_pass_target
        else:
            if verbose:
                print(f"    Current worry level is not divisible by {self.test_divisor}.")
                print(f"    Item with worry level {item} is thrown to monkey {self.test_fail_target}.")
            return self.test_fail_target

    def __str__(self) -> str:
        return f"monke"


# things
monkeys: list[Monkey] = []


# functions
def load_monkeys() -> None:
    lines = open("11.txt").read().split("\n")
    i = 0
    while i < len(lines):
        # "Monkey X:"
        i += 1
        # "  Starting items: [n,n,...]"
        a = lines[i].split(":")[1].replace(" ", "").split(",")
        list_int = []
        for s in a:
            list_int.append(int(s))
        i += 1
        # "  Operation: new = old [*/+] [n]"
        b = lines[i].split(" = old ")[1]
        operator_is_add = b.split(" ")[0] == "+"  # + or *
        b2 = b.split(" ")[1]
        operand = 0
        if b2 != "old":
            operand = int(b2)
        i += 1
        # "  Test: divisible by [n]"
        c = lines[i].split("by ")[1]
        test_divisor = int(c)
        i += 1
        # "    If true: throw to monkey [n]"
        d = lines[i].split("monkey ")[1]
        test_pass_target = int(d)
        i += 1
        # "    If false: throw to monkey [n]"
        e = lines[i].split("monkey ")[1]
        test_fail_target = int(e)
        i += 1
        # ""
        i += 1
        m = Monkey(
            list_int,
            operator_is_add,
            operand,
            test_divisor,
            test_pass_target,
            test_fail_target
        )
        monkeys.append(m)


def do_round():
    # for each monkey
    m = 0
    for monkey in monkeys:
        if verbose:
            print(f"Monkey {m}:")
        # for each item in monkey's list:
        item_count = len(monkey.items)
        for i in range(item_count):
            item = monkey.items.pop(0)
            # perform that monkey's operation (inspection)
            item = monkey.operation(item)
            # divide by 3 as monkey gets bored (part 1 only)
            if part1:
                item = item // 3
            # perform test
            monkeys[monkey.test(item)].items.append(item)
        m += 1
        if verbose:
            print("")


def solve():
    # sort monkeys by items inspected
    monkeys.sort(key=lambda monke: monke.items_inspected, reverse=True)
    # multiply two monkeys who inspected the most
    monkey_business = monkeys[0].items_inspected * monkeys[1].items_inspected
    # output answer
    print(str(monkey_business))


# setup
load_monkeys()

rounds = 20 if part1 else 10000
start = time()
for round in range(rounds):
    do_round()
    if round % 1 == 0:
        time_str = str(time() - start)[0:5]
        print(f"{time_str}: Completed round {round}.")
solve()
