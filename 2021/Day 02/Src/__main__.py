""" Day 02 of the 2021 Advent of Code
https://adventofcode.com/2021/day/2
https://adventofcode.com/2021/day/2/input
Did some cleanup on day 4, also added recursive alternatives for practice
"""

import sys

sys.setrecursionlimit(1500)


def clean_line(line):
    line = line.split()
    line[0] = line[0].strip()
    line[1] = int(line[1])
    return line


def load_data(Path):
    data_list = []
    with open(Path, "r") as file:
        [data_list.append(clean_line(line)) for line in file]
    return data_list


def part_1_recursive(moves, horizontal=0, depth=0):
    move = moves[0][0]
    distance = moves[0][1]
    if move == "forward":
        horizontal += distance
    if move == "down":
        depth += distance
    if move == "up":
        depth -= distance

    if len(moves) > 1:
        return part_1_recursive(moves[1:], horizontal, depth)
    return horizontal * depth


def part_1(moves):
    horizontal = 0
    depth = 0

    for move, distance in moves:
        if move == "forward":
            horizontal += distance
        if move == "down":
            depth += distance
        if move == "up":
            depth -= distance

    solution = horizontal * depth
    return solution


def part_2_recursive(moves, horizontal=0, depth=0, aim=0):
    move = moves[0][0]
    distance = moves[0][1]
    if move == "forward":
        horizontal += distance
        depth += distance * aim
    if move == "down":
        aim += distance
    if move == "up":
        aim -= distance

    if len(moves) > 1:
        return part_2_recursive(moves[1:], horizontal, depth, aim)
    return horizontal * depth


def part_2(moves):
    aim = 0
    horizontal = 0
    depth = 0

    for move, distance in moves:
        if move == "forward":
            horizontal += distance
            depth += distance * aim
        if move == "down":
            aim += distance
        if move == "up":
            aim -= distance
    solution = horizontal * depth
    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 150
    assert part_1(data) == 1989014
    assert part_1_recursive(data_test) == 150
    assert part_1_recursive(data) == 1989014

    assert part_2(data_test) == 900
    assert part_2(data) == 2006917119
    assert part_2_recursive(data_test) == 900
    assert part_2_recursive(data) == 2006917119


if __name__ == "__main__":
    main()
