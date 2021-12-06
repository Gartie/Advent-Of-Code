""" Day 06 of the 2021 Advent of Code
https://adventofcode.com/2021/day/6
https://adventofcode.com/2021/day/6/input

We have some fishes, they produce a new fish each every 6 days.
New fishes take 8 days to produce their first fish, after that it takes the 6 days.

The fishes might mutate even faster than this code if they keep at it..

I solved part one with part_1(), witch was a bit naive but allright.
part_1() started to cook my machine with the number of itterations requerd for part two.

For part two i tried a 'rolling' list before i turned to maths, lo and behold, it worked!

After the second star and some fistbumps
    i cleaned part_2 a bit and turned it into simulate_fish_population().
"""

import numpy as np


def load_data(path):
    with open(path, "r") as file:
        content = file.read()
    content_list = content.split(",")
    data_list = np.array([int(i.strip()) for i in content_list if i.strip()], dtype=int)
    return data_list


def part_1(data, number_of_days=80):
    # dont try this at home, fries my pc at 170 itterations :(
    for _ in range(number_of_days):
        number_of_births = (data == 0).sum()
        data = data - 1
        data = np.where(data == -1, 6, data)
        data = np.concatenate((data, [8] * number_of_births))

    solution = len(data)
    return solution


def part_2(data, number_of_days=80):
    """Function as used to solve part 2 of the AoC challange
    Using hardcoded values and logic, solved that in simulate_fish_population()
    """
    fishes = np.zeros((9), dtype=np.ulonglong)
    for i in data:
        fishes[i] += 1

    for _ in range(number_of_days):
        number_of_births = fishes[0]
        fishes[0] = fishes[1]
        fishes[1] = fishes[2]
        fishes[2] = fishes[3]
        fishes[3] = fishes[4]
        fishes[4] = fishes[5]
        fishes[5] = fishes[6]
        fishes[6] = fishes[7] + number_of_births
        fishes[7] = fishes[8]
        fishes[8] = number_of_births

    return sum(fishes)


def init_fishes(data, length):
    fishes = np.zeros((length), dtype=np.ulonglong)
    for i in data:
        fishes[i] += 1
    return fishes


def simulate_fish_population(
    data, number_of_days=80, post_birth_val=6, new_fish_val=8, fishes=None
):
    """More generic version of part_2_original()"""
    if fishes is None:
        fishes = init_fishes(data, max(post_birth_val, new_fish_val) + 1)
        # print(fishes, 'start')

    if not number_of_days:
        if fishes is None:
            return None
        return sum(fishes)

    fishes_lenth = len(fishes)
    number_of_births = fishes[0]
    for i in range(fishes_lenth):

        if i < fishes_lenth - 1:
            fishes[i] = fishes[i + 1]

        if post_birth_val == i:
            if post_birth_val >= new_fish_val:
                fishes[i] = 0
            fishes[i] = fishes[i] + number_of_births

        if new_fish_val == i:
            if new_fish_val > post_birth_val:
                fishes[i] = 0
            fishes[i] = number_of_births

    return simulate_fish_population(
        data=None,
        number_of_days=number_of_days - 1,
        fishes=fishes,
        post_birth_val=post_birth_val,
        new_fish_val=new_fish_val,
    )


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    # part 1
    assert part_1(data_test, 18) == 26
    assert part_1(data, 80) == 349549

    # part 2 with part one examples and results
    assert part_2(data_test, 18) == 26
    assert part_2(data_test, 80) == 5934
    assert part_2(data, 80) == 349549

    # part_2() with part 2 vaules
    assert part_2(data_test, 256) == 26984457539
    assert part_2(data, 256) == 1589590444365

    # simulate_fish_population() with part one examples and results
    assert simulate_fish_population(data_test, 18) == 26
    assert simulate_fish_population(data_test, 80) == 5934
    assert simulate_fish_population(data, 80) == 349549
    assert simulate_fish_population(data_test, 256) == 26984457539
    assert simulate_fish_population(data, 256) == 1589590444365


if __name__ == "__main__":
    main()
