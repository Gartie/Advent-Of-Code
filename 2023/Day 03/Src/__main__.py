""" Day 3 of the 2023 Advent of Code
https://adventofcode.com/2023/day/3
https://adventofcode.com/2023/day/3/input """

import re
from dataclasses import dataclass
from typing import List


@dataclass
class Part_position:
    # Value of code
    value: int = 0
    # Row in matrix
    r: int = 0
    # Starting column in matrix
    c: int = 0
    # Length of value
    length: int = 0


def load_data(Path):
    data_list = []
    with open(Path, "r") as file:
        [data_list.append("." + line.strip() + ".") for line in file]

    data_list.insert(0, "." * len(data_list[0]))
    data_list.append("." * len(data_list[0]))

    return data_list


def get_part_positions(matrix, expression):
    positions = []

    curr_code = ""
    for r_inx, row in enumerate(matrix):
        for c_inx, char in enumerate(row):
            match = re.match(expression, char) != None

            if match:
                curr_code += char
            if not match and len(curr_code) > 0:
                positions.append(
                    Part_position(
                        curr_code, r_inx, c_inx - len(curr_code), len(curr_code)
                    )
                )
                curr_code = ""

    return positions


def get_engines(data):
    engines = get_part_positions(data, "\d")
    return engines
    

def get_gears(data):
    engines = get_part_positions(data, "\*")
    return engines


def get_adjacent_values(matrix, r, c, length):
    s = ""

    # Above
    s += matrix[r - 1][c - 1 : c + length + 1 :]
    # Below
    s += matrix[r + 1][c - 1 : c + length + 1 :]
    # Left
    s += matrix[r][c - 1]
    # Right
    s += matrix[r][c + length]

    return s


def parts_adjacent(part1, part2):
    if abs(part1.r - part2.r) > 1:
        return False
    
    f1 = part1.c-1
    l1 = part1.c+part1.length
    f2 = part2.c
    l2 = part2.c+part2.length-1
    
    return f1 <= l2 and l1 >= f2


def part_1(data):
    solution = 0

    for part in get_engines(data):
        adjacent = get_adjacent_values(data, part.r, part.c, part.length)
        # print(e.value, "-", adjacent)
        if not adjacent.replace(".", "") == "":
            solution += int(part.value)

    return solution


def part_2(data):
    solution = 0
    
    engines = get_engines(data)
    for gear in get_gears(data):
        adjacent_to_gear = get_adjacent_values(data, gear.r, gear.c, gear.length)

        # There must be atleast two digets ajacent to the gear, otherwise the cannot me two engines adjacent
        if len([ad for ad in adjacent_to_gear if ad.isdigit()]) < 2:
            continue

        adjacent_values = []
        for engine in engines:
            if parts_adjacent(gear, engine):
                adjacent_values.append(int(engine.value))
         
        if len(adjacent_values) >= 2:
            solution += adjacent_values[0]*adjacent_values[1]
    
    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 4361
    assert part_1(data) == 532428
    assert part_2(data_test) == 467835
    assert part_2(data) == 84051670


if __name__ == "__main__":
    main()
