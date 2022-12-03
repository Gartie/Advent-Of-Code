""" Day 01 of the 2022 Advent of Code
https://adventofcode.com/2022/day/01
https://adventofcode.com/2022/day/01/input """


def load_data(Path):
    data_list = []
    with open(Path, "r") as file:
        elf_list = file.read().split("\n\n")

        for elf in elf_list:
            data_list.append([])
            for cal in elf.split("\n"):
                data_list[-1].append(int(cal))

    return data_list


def part_1(data):
    solution = None

    solution = max([sum(elf) for elf in data])

    return solution


def part_2(data):
    solution = None

    elfs = [sum(elf) for elf in data]
    elfs.sort(reverse=True)
    solution = sum(elfs[0:3])

    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 24000
    assert part_1(data) == 70296
    assert part_2(data_test) == 45000
    assert part_2(data) == 205381

    # print(part_1(data_test))
    # print(part_1(data))
    # print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
