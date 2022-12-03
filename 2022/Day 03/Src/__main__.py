""" Day 03 of the 2022 Advent of Code
https://adventofcode.com/2022/day/3
https://adventofcode.com/2022/day/3/input """

import string


def load_data(Path):
    data_list = []
    with open(Path, "r") as raw_file:
        data_list = raw_file.read().split("\n")

    return data_list


def get_char_value(char):
    try:
        return string.ascii_lowercase.index(char) + 1
    except:
        return string.ascii_uppercase.index(char) + 26 + 1


def get_intersection(a, b):
    char = set(a).intersection(b)
    char = "".join(char)
    return char


def part_1(data):
    solution = None

    values = []
    for sack in data:
        sep = int(len(sack) / 2)
        char = get_intersection(sack[0:sep], sack[sep:])
        values.append(get_char_value(char))

    solution = sum(values)
    return solution


def part_2(data):
    solution = None

    values = []
    for i in range(0, len(data), 3):
        char = data[i]
        char = get_intersection(char, data[i + 1])
        char = get_intersection(char, data[i + 2])
        values.append(get_char_value(char))

    solution = sum(values)
    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 157
    assert part_1(data) == 7908
    assert part_2(data_test) == 70
    assert part_2(data) == 2838

    # print(part_1(data_test))
    # print(part_1(data))
    # print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
