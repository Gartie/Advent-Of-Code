""" Day 10 of the 2022 Advent of Code
https://adventofcode.com/2022/day/10
https://adventofcode.com/2022/day/10/input

Needs some tinkering!

tst output  (Schifted left 1, not line 0)
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......###.
#######.......#######.......#######.....

Prod Output (Schifted left 1, not line 0)
####..##...##..#..#.####.###..####..##..
#....#..#.#..#.#..#....#.#..#.#....#..#.
###..#....#....#..#...#..#..#.###..#....
.....#.##.#....#..#..#...###..#....#....
.....#..#.#..#.#..#.#....#.#..#....#..#.
......###..##...##..####.#..#.####..##..
"""


def load_data(Path):
    data_list = []
    with open(Path, "r") as file:
        lines = file.read().split("\n")

    for line in lines:
        if not line.strip():
            continue
        if "addx" in line:
            _, value = line.split()
            value = int(value)
            data_list.append(value)
        else:
            data_list.append(0)
    return data_list


def part_1(data):
    solution = []
    cycle = 0
    register = 1

    for value in data:
        cycle += 1
        if (cycle - 20) % 40 == 0:
            solution.append(cycle * register)
        if value:
            cycle += 1
            if (cycle - 20) % 40 == 0:
                solution.append(cycle * register)

            register += value

    return sum(solution)


def do_print(cycle, register, chunck_size=40):
    return abs(register - (cycle % chunck_size) + 1) < 2


def chop_up_list(list, chunck_size=40):
    pos = 0
    solution = ""
    while pos < len(list) - 1:
        if solution:
            solution = solution + "\n"
        solution = solution + "".join(list[pos : pos + chunck_size])
        pos += chunck_size
    return solution


def part_2(data):
    chunck_size = 40
    solution = ["." for _ in range(chunck_size * 6)]
    cycle = 0
    register = 1

    for value in data:
        cycle += 1
        if do_print(cycle, register):
            solution[cycle - 1] = "#"

        if value:
            cycle += 1
            if do_print(cycle, register):
                solution[cycle - 1] = "#"

            register += value
            register = register % chunck_size

    return chop_up_list(solution)


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 13140
    assert part_1(data) == 17380

    print(part_2(data_test))
    print()
    print(part_2(data))


if __name__ == "__main__":
    main()
