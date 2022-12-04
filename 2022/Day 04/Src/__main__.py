""" Day 04 of the 2022 Advent of Code
https://adventofcode.com/2022/day/4
https://adventofcode.com/2022/day/4/input """


import re


def load_data(Path):
    data_list = []

    with open(Path, "r") as raw_file:
        file = raw_file.read().split("\n")

    for line in file:

        left_left, left_right, right_left, right_right = re.split(",|-", line)

        left_left = int(left_left)
        left_right = int(left_right)
        right_left = int(right_left)
        right_right = int(right_right)

        left = [left_left, left_right]
        right = [right_left, right_right]
        data_list.append([left, right])

    return data_list


def is_larger(left, right):
    output = False

    # Left is larger than right
    if left[0] <= right[0] and left[1] >= right[1]:
        output = True
    # Right is larger than left
    elif right[0] <= left[0] and right[1] >= left[1]:
        output = True

    return output


def is_overlap(left, right):
    output = False

    # Left overlaps Right
    if left[1] >= right[0] and left[0] <= right[1]:
        output = True
    # Right overlaps left
    elif right[0] <= left[1] and right[1] >= left[0]:
        output = True

    return output


def part_1(data):
    solution = 0

    for pair in data:
        if is_larger(pair[0], pair[1]):
            solution += 1

    return solution


def part_2(data):
    solution = 0

    for pair in data:
        if is_overlap(pair[0], pair[1]):
            solution += 1

    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 2
    assert part_1(data) == 573
    assert part_2(data_test) == 4
    assert part_2(data) == 867

    # print(part_1(data_test))
    # print(part_1(data))
    # print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
