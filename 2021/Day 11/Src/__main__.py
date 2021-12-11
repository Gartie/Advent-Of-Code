""" Day 11 of the 2021 Advent of Code
https://adventofcode.com/2021/day/11
https://adventofcode.com/2021/day/11/input """

from dataclasses import dataclass


@dataclass
class Octopus:
    """Class for keeping track of octo's."""

    line_index: int
    char_index: int
    value: int = -1


def load_data(path):
    data_list = []
    with open(path, "r") as file:
        for line in file:
            line_word_list = []
            line = line.strip()
            for char in line:
                line_word_list.append(int(char))
            data_list.append(line_word_list)
    return data_list


def get_surrounding_octo(data, octopus, boundary):
    found_octos = []

    c_index = octopus.char_index
    l_index = octopus.line_index
    line = data[l_index]

    for line_offset in [-1, 0, +1]:
        for char_offset in [-1, 0, +1]:

            if not line_offset and not char_offset:
                continue

            found_c = c_index + char_offset
            found_l = l_index + line_offset

            if found_c in (-1, len(line)):
                continue
            if found_l in (-1, len(data)):
                continue

            value = int(data[found_l][found_c])
            if value != boundary:
                found_octos.append(Octopus(found_l, found_c, value))

    return found_octos


def flash(data, flash_count=0):
    for l_index, line in enumerate(data):
        for c_index, char in enumerate(line):
            if char <= 9:
                continue

            flash_count += 1
            surrounding_octo = get_surrounding_octo(data, Octopus(l_index, c_index), -1)
            data[l_index][c_index] = -1
            for octo in surrounding_octo:
                data[octo.line_index][octo.char_index] += 1

    for line in data:
        for char in line:
            if char > 9:
                return flash(data, flash_count)
    return data, flash_count


def simulate_flashes(data, itterations=100, is_part_2=False):
    solution = 0
    step_count = 0
    while step_count < itterations or is_part_2:
        step_count += 1

        # All octo's increase 1 in charge
        for l_index, line in enumerate(data):
            for c_index in range(len(line)):
                data[l_index][c_index] += 1

        # Process the flash chain reaction
        data, local_flash_count = flash(data, flash_count=0)
        solution += local_flash_count

        # Reset flashed octos to value 0
        for l_index, line in enumerate(data):
            for c_index in range(len(line)):
                if data[l_index][c_index] == -1:
                    data[l_index][c_index] = 0

        if is_part_2:
            all_zeros_found = True
            for l_index, line in enumerate(data):
                if not all_zeros_found:
                    break
                for c_index in range(len(line)):
                    if data[l_index][c_index] != 0:
                        all_zeros_found = False
                        break
            is_part_2 = not all_zeros_found

    return solution, step_count


def part_1(data, itterations):
    solution, _ = simulate_flashes(data, itterations, is_part_2=False)
    return solution


def part_2(data):
    _, solution = simulate_flashes(data, is_part_2=True)
    return solution


def main():
    # Reloading the data for each excecution, because of a bug i didn't feel like solving.
    # Should implement a class

    data_test = load_data("..//Data//Test.txt")
    assert part_1(data_test, 10) == 204

    data_test = load_data("..//Data//Test.txt")
    assert part_1(data_test, 100) == 1656

    data = load_data("..//Data//Prod.txt")
    assert part_1(data, 100) == 1723

    data_test = load_data("..//Data//Test.txt")
    assert part_2(data_test) == 195

    data = load_data("..//Data//Prod.txt")
    assert part_2(data) == 327


if __name__ == "__main__":
    main()
