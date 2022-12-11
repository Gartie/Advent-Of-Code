""" Day 11 of the 2022 Advent of Code
https://adventofcode.com/2022/day/11
https://adventofcode.com/2022/day/11/input """


from dataclasses import dataclass, field
from math import floor, prod, lcm


@dataclass
class Monkey:
    raw_monkey: str = field(repr=False)
    relieve: bool
    upper_limit_item: int = 0
    items: list = field(default_factory=list)
    operation_oparator: str = ""
    operation_value: int = 0
    test_value: int = 0
    monkey_index_true: int = 0
    monkey_index_false: int = 0
    inspections: int = 0

    def __post_init__(self):
        lines = self.raw_monkey.split("\n")
        lines = [line.strip() for line in lines]
        lines[1] = lines[1][16:]
        lines[1] = lines[1].replace(" ", "")
        self.items = [int(value) for value in lines[1].split(",")]
        self.test_value = int(lines[3][19:])
        self.monkey_index_true = int(lines[4][24:])
        self.monkey_index_false = int(lines[5][25:])
        self.operation_oparator, opp_value = lines[2][21:].split(" ")
        if opp_value == "old":
            self.operation_value = 0
        else:
            self.operation_value = int(opp_value)

    def inspect_items(self):
        self.inspections = self.inspections + len(self.items)
        item_list = []
        for item in self.items:
            destination = -1
            value = -1

            # determin the righthand value of the equation
            if not self.operation_value:
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

            # prevent overflow and delays due to large value
            """ Post goldenstars ajustment
            At first i used the following 2 lines to reduce value, thinking that % would cause issues
            # while value > LCM:
            #     value -= LCM
            
            After study-ing and running code written by Bas Langenberg, i implemented %=
            This reduced the running time of part 2, dramaticly! From an hour, to a second!
            https://github.com/BasLangenberg/aoc/blob/main/python/2022/11/day-p2.py
            """
            value %= self.upper_limit_item

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
    test_values = [monkey.test_value for monkey in monkeys]
    LCM = lcm(*[monkey.test_value for monkey in monkeys])

    for monkey in monkeys:
        monkey.upper_limit_item = LCM

    for x in range(rounds):
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

    # Part 1
    assert part_x(data_test, relieved_part_1, rounds_part_1) == 10605
    assert part_x(data, relieved_part_1, rounds_part_1) == 66802
    # Part 2
    assert part_x(data_test, relieved_part_2, rounds_part_2) == 2713310158
    assert part_x(data, relieved_part_2, rounds_part_2) == 21800916620


if __name__ == "__main__":
    main()
