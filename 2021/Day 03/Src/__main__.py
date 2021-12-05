""" Day 03 of the 2021 Advent of Code
https://adventofcode.com/2021/day/3
https://adventofcode.com/2021/day/3/input
Today i used recursion succesfully for the first time ever!
"""
from collections import Counter


def load_data(path):
    data_list = []
    with open(path, "r") as file:
        [data_list.append(line.strip()) for line in file]
    return data_list


def get_mostcommon_vertical(data):
    most_common_list = []
    for i in data:
        most_common = Counter(i).most_common(2)
        if len(most_common) == 1:
            most_common_list.append(str(most_common[0][0]))
            continue
        if most_common[0][1] == most_common[1][1]:
            most_common_list.append(str(1))
            continue
        most_common_list.append(str(most_common[0][0]))
    return "".join(most_common_list)


def inverse_bitstring(string):
    inverse = []
    for i in string:
        if i == "1":
            inverse.append("0")
        else:
            inverse.append("1")
    return "".join(inverse)


def pivot_matrix(data):
    if data:
        out_data = [[] for q in data[0]]
    else:
        out_data = []
    for line in data:
        for i, bit in enumerate(line):
            out_data[i].append(bit)
    out_data = ["".join(d) for d in out_data]
    return out_data


def part_1(data):
    solution = None
    data = pivot_matrix(data)
    gamma = get_mostcommon_vertical(data)
    epsilon = inverse_bitstring(gamma)
    solution = int(gamma, 2) * int(epsilon, 2)
    return solution


def flip_bit(bit):
    return int(not int(bit))


def filter_list(data, position=0, inverse_filter=False):
    value = int(get_mostcommon_vertical(pivot_matrix(data))[position])
    if inverse_filter:
        value = flip_bit(value)
    out_list = [i for i in data if str(i[position]) == str(value)]
    if len(out_list) == 0:
        raise ProcessError("Filter ended with 0 values.")
    if len(out_list) == 1:
        return out_list[0]

    return filter_list(out_list, position=position + 1, inverse_filter=inverse_filter)


def part_2(data):
    solution = None

    gamma_filter = filter_list(data, position=0, inverse_filter=False)
    epsilon_filter = filter_list(data, position=0, inverse_filter=True)

    solution = int(gamma_filter, 2) * int(epsilon_filter, 2)
    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    assert part_1(data_test) == 198
    assert part_1(data) == 2724524
    assert part_2(data_test) == 230
    assert part_2(data) == 2775870


if __name__ == "__main__":
    main()
