""" Day 11 of the 2022 Advent of Code
https://adventofcode.com/2022/day/11
https://adventofcode.com/2022/day/11/input """


from dataclasses import dataclass, field
from math import floor, prod


@dataclass
class Monkey:
    raw_monkey: str = field(repr=False)
    relieve: bool
    name: str = ""
    index: int = 0
    items: list = field(default_factory=list)
    operation_oparator: str = ""
    operation_value: str = ""
    test_value: str = ""
    monkey_index_true: int = 0
    monkey_index_false: int = 0
    inspections: int = 0

    def __post_init__(self):
        lines = self.raw_monkey.split("\n")
        lines = [line.strip() for line in lines]

        lines[1] = lines[1][16:]
        lines[1] = lines[1].replace(" ", "")
        self.items = [int(value) for value in lines[1].split(",")]

        self.name = lines[0].strip(":")
        self.index = int(self.name[6:])

        self.operation_oparator, opp_value = lines[2][21:].split(" ")
        if opp_value == "old":
            self.operation_value = 0
        else:
            self.operation_value = int(opp_value)

        self.test_value = int(lines[3][19:])
        self.monkey_index_true = int(lines[4][24:])
        self.monkey_index_false = int(lines[5][25:])

    def inspect_items(self):
        self.inspections = self.inspections + len(self.items)
        item_list = []
        for item in self.items:
            destination = -1
            value = -1

            # determin the righthand value of the equation
            if self.operation_value:
                value = item
            else:
                value = self.operation_value

            # determin type and do oparation
            if self.operation_oparator == "*":
                value = item * value
            elif self.operation_oparator == "+":
                value = item + value
            else:
                raise TypeError(
                    "Operation_oparator unknown: " + self.operation_oparator
                )

            LCM = 9699690
            while value > LCM:
                value -= LCM

            # calm down and devide by 3, or dont and panic about int overruns!
            if self.relieve:
                value = floor(value / 3)

            # determin destination
            if value % self.test_value == 0:
                destination = self.monkey_index_true
            else:
                destination = self.monkey_index_false

            item_list.append((destination, value))

        self.items = []
        return item_list


def load_data(Path):
    data_list = []
    with open(Path, "r") as file:
        data_list = file.read().split("\n\n")

    return data_list


def part_x(raw_monkeys, relieve, rounds):
    solution = None
    monkeys = [Monkey(monkey, relieve) for monkey in raw_monkeys]

    for x in range(rounds):
        if x and x % 100 == 0:
            print("Still working, on", x, "now")
        for monkey in monkeys:
            items = monkey.inspect_items()
            for destination, value in items:
                monkeys[destination].items.append(value)

    mb_list = [monkey.inspections for monkey in monkeys]
    mb_list.sort(reverse=True)
    solution = prod(mb_list[0:2])

    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    relieved_part_1 = True
    relieved_part_2 = False
    rounds_part_1 = 20
    rounds_part_2 = 10000

    assert part_x(data_test, relieved_part_1, rounds_part_1) == 10605
    assert part_x(data, relieved_part_1, rounds_part_1) == 66802

    print("This does take a while, but does work :)")
    assert part_x(data, relieved_part_2, rounds_part_2) == 21800916620


if __name__ == "__main__":
    main()
