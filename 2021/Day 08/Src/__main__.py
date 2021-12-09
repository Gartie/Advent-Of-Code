""" Day 08 of the 2021 Advent of Code
https://adventofcode.com/2021/day/8
https://adventofcode.com/2021/day/8/input """


def load_data(path):
    data_list = []
    with open(path, "r") as file:
        for line in file:
            ref_values, values = line.split(" | ")

            ref_values = ref_values.split(" ")
            ref_values = [i.strip() for i in ref_values]
            ref_values = sorted(ref_values, key=len)
            ref_values = ["".join(sorted(i, key=str.lower)) for i in ref_values]
            assert len(ref_values) == 10

            values = values.split(" ")
            values = [i.strip() for i in values]
            values = ["".join(sorted(i, key=str.lower)) for i in values]
            assert len(values) == 4

            data_list.append((ref_values, values))

    return data_list


def value_in_value(ref, value):
    for i in ref:
        if not i in value:
            return False
    return True


def value_minus_value(value, min_value):
    for i in min_value:
        value = value.replace(i, "")
    return value


def order_ref_values(ref_values):
    values_order = [None] * 10

    len_5 = ref_values[3 : 5 + 1]
    len_6 = ref_values[6 : 8 + 1]

    # 1
    rechts = ref_values[0]
    values_order[1] = rechts
    values_order[4] = ref_values[2]
    values_order[7] = ref_values[1]
    values_order[8] = ref_values[9]

    # 2
    values_order[3] = [i for i in len_5 if value_in_value(values_order[1], i)][0]
    values_order[6] = [i for i in len_6 if not value_in_value(values_order[1], i)][0]

    # 3
    rechts_boven = value_minus_value(values_order[8], values_order[6])
    values_order[2] = [i for i in len_5 if not value_in_value(values_order[1], i)
                                and value_in_value(rechts_boven, i)][0]
    values_order[5] = [i for i in len_5 if not value_in_value(values_order[1], i)
                                and not value_in_value(rechts_boven, i)][0]

    # 4
    links = value_minus_value(values_order[8], values_order[3])
    values_order[9] = [i for i in len_6 if value_in_value(values_order[1], i)
                                and not value_in_value(links, i)][0]

    values_order[0] = [i for i in len_6 if value_in_value(values_order[1], i)
                                and value_in_value(links, i)][0]

    return values_order


def part_1(data):
    solution = 0

    for i in data:
        for value in i[1]:
            if len(value) in [2, 4, 3, 7]:
                solution = solution + 1

    return solution


def part_2(data):
    solution = 0

    for line in data:
        line_number = ""
        ordered_ref = order_ref_values(line[0])

        for value in line[1]:

            for index in range(10):
                if value == ordered_ref[index]:
                    line_number = line_number + str(index)
                    break

        solution = solution + int(line_number)

    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 26
    assert part_1(data) == 445
    assert part_2(data_test) == 61229
    assert part_2(data) == 1043101


if __name__ == "__main__":
    main()
