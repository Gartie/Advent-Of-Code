""" Day 04 of the 2021 Advent of Code
https://adventofcode.com/2021/day/4
https://adventofcode.com/2021/day/4/input 

First use (in AoC) of an external package
"""

import numpy as np
from pprint import pprint


def load_data(path):
    bingoball_list = []
    data_list = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()

            if "," in line:
                bingoball_list = [int(ball) for ball in line.split(",")]
                continue

            if not line:
                data_list.append([])	
                continue

            data_list[-1].append([])
            line = line.replace("  ", " ")
            line_list = line.split(" ")
            data_list[-1][-1] = [int(i) for i in line_list]
        list = [np.array(i) for i in data_list]
    return list, bingoball_list


def stamp_card(card, ball, stamp=-1):
    card = np.where(card == ball, stamp, card)
    return card


def check_card(card):
    card_len = len(card[0])
    
    collumns = card.sum(axis=0)
    rows = card.sum(axis=1)
    value_to_find = -1 * card_len
    BINGOOOOOOO = value_to_find in collumns or value_to_find in rows
    return BINGOOOOOOO


def play_card(card, balls, played_balls=0):
    played_balls = played_balls + 1
    card = stamp_card(card, balls[0])

    if not check_card(card):
        return play_card(card, balls[1:], played_balls)

    card = stamp_card(card, -1, stamp=0)
    return (played_balls, balls[0], card.sum())


def part_1(cards, balls, get_best=True):
    solution = None

    fastest = (0, 0, 0)
    slowest = (0, 0, 0)
    for card in cards:
        current = play_card(card, balls)
        if current[0] < fastest[0] or not fastest[0]:
            fastest = current
        if current[0] > slowest[0] or not slowest[0]:
            slowest = current

    solution = slowest[1] * slowest[2]
    if get_best:
        solution = fastest[1] * fastest[2]
    return solution


def part_2(cards, balls):
    solution = part_1(cards, balls, get_best=False)
    return solution


def main():
    data, balls = load_data("..//Data//Prod.txt")
    data_test, balls_test = load_data("..//Data//Test.txt")

    assert part_1(data_test, balls_test) == 4512
    assert part_1(data, balls) == 22680
    assert part_2(data_test, balls_test) == 1924
    assert part_2(data, balls) == 16168


if __name__ == "__main__":
    main()
