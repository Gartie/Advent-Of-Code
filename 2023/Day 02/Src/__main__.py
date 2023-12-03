""" Day 2 of the 2023 Advent of Code
https://adventofcode.com/2023/day/2
https://adventofcode.com/2023/day/2/input """

from dataclasses import dataclass
from typing import List


@dataclass
class Round:
    r: int = 0
    g: int = 0
    b: int = 0


@dataclass
class Game:
    id: int
    rounds: List[Round]


def load_data_line_to_id(line):
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    id = line.split(":")[0].split(" ")[1]
    return int(id)


def load_data_line_to_rounds(line):
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    rounds = []
    line = line.split(":")[1]
    # 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    text_rounds = [l.strip() for l in line.split(";")]
    # 8 green, 6 blue, 20 red
    # 5 blue, 4 red, 13 green
    # 5 green, 1 red
    draw_in_round = []
    for text_round in text_rounds:
        text_draws = text_round.split(", ")
        # 8 green
        # 6 blue
        # 20 red
        round = Round()
        for text_draw in text_draws:
            count, color = text_draw.split()
            if color == "red":
                round.r = round.r + int(count)
            if color == "green":
                round.g = round.g + int(count)
            if color == "blue":
                round.b = round.b + int(count)
        rounds.append(round)

    return rounds


def load_data_line_to_Game(line):
    return Game(load_data_line_to_id(line), load_data_line_to_rounds(line))


def load_data(Path):
    data_list = []
    with open(Path, "r") as file:
        data_list = [load_data_line_to_Game(line.strip()) for line in file]
    return data_list


def part_1(data):
    solution = 0

    max_r = 12
    max_g = 13
    max_b = 14

    for g in data:
        for l in g.rounds:
            if l.r > max_r or l.g > max_g or l.b > max_b:
                break
        else:
            solution = solution + g.id

    return solution


def part_2(data):
    solution = 0
    powers = []

    for g in data:
        min_r = 0
        min_g = 0
        min_b = 0

        for l in g.rounds:
            if l.r > min_r:
                min_r = l.r
            if l.g > min_g:
                min_g = l.g
            if l.b > min_b:
                min_b = l.b

        powers.append(min_b * min_g * min_r)

    solution = sum(powers)
    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 8
    assert part_1(data) == 2176
    assert part_2(data_test) == 2286
    assert part_2(data) == 63700


if __name__ == "__main__":
    main()
