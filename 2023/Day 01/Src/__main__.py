""" Day 1 of the 2023 Advent of Code
https://adventofcode.com/2023/day/1
https://adventofcode.com/2023/day/1/input """


def load_data(Path):
    data_list = []
    with open(Path, "r") as file:
        [data_list.append(line.strip()) for line in file]
    return data_list


def add_digets_to_letters(input):
    replacements = [
        ["one", "o1ne"],
        ["two", "t2wo"],
        ["three", "th3ree"],
        ["four", "fo4ur"],
        ["five", "fi5ve"],
        ["six", "si6x"],
        ["seven", "sev7en"],
        ["eight", "eig8ht"],
        ["nine", "ni9ne"],
    ]

    for rep in replacements:
        input = input.replace(rep[0], rep[1])

    return input


def solve(input, with_replace):
    total = 0
    for line in input:
        if line.strip() == "":
            continue

        if with_replace:
            line = add_digets_to_letters(line)

        ds = [diget for diget in line if diget in "123456789"]
        total = total + int(ds[0] + ds[-1])

    return total


def part_1(data):
    solution = None
    solution = solve(data, False)
    return solution


def part_2(data):
    solution = None
    solution = solve(data, True)
    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test_part_one = load_data("..//Data//TestP1.txt")
    data_test_part_two = load_data("..//Data//TestP2.txt")

    assert part_1(data_test_part_one) == 142
    assert part_1(data) == 55538
    assert part_2(data_test_part_two) == 281
    assert part_2(data) == 54875


if __name__ == "__main__":
    main()
