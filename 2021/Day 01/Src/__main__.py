""" Day 01 of the 2021 Advent of Code
https://adventofcode.com/2021/day/1
https://adventofcode.com/2021/day/1/input """


def get_increase_decrease(list_int):
    previous_number = -1
    count_increase = 0
    for current_number in list_int:
        if previous_number == -1:
            previous_number = current_number
            continue

        if current_number > previous_number:
            count_increase = count_increase + 1

        previous_number = current_number

    return count_increase


def get_increase(data):
    result = len([1 for n, i in enumerate(data[1:]) if i > data[n]])
    return result


def load_from_file(file_name):
    with open(file_name, "r") as file:
        file = [int(f.strip()) for f in file]
    return file


def get_groups(in_list, size=3):
    out_list = []
    for index, value in enumerate(in_list):
        sub_list = []
        for i in range(0, size):
            try:
                v = in_list[index + i]
                sub_list.append(v)
            except IndexError:
                break
        if len(sub_list) == size:
            out_list.append(sub_list)
    return out_list


def part_1(data):
    return get_increase(data)


def part_2(data):
    groups = get_groups(data)
    data = [sum(x) for x in groups]
    solution = get_increase(data)
    return solution


def main():
    data_test = load_from_file("../Data/test.txt")
    data = load_from_file("../Data/prod.txt")

    assert part_1(data_test) == 7
    assert part_1(data) == 1688
    assert part_2(data_test) == 5
    assert part_2(data) == 1728


if __name__ == "__main__":
    main()
