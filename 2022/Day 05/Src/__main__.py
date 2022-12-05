""" Day 05 of the 2022 Advent of Code
https://adventofcode.com/2022/day/5
https://adventofcode.com/2022/day/5/input """


def load_data(Path):
    with open(Path, "r") as raw_file:
        file = raw_file.read().split("\n")

    movements = []
    stacks = []

    for line in file:

        # skip empty line to prevent index errors
        if not line.strip():
            continue

        # Process stacks layer
        if "[" in line:
            # Init stacks
            if len(stacks) == 0:
                # each stack takes up 4 chars '[A] '
                # Except for the last one so we add 1
                no_of_stacks = (len(line) + 1) / 4
                no_of_stacks = int(no_of_stacks)
                stacks = [[] for i in range(no_of_stacks)]

            # Add values to stacks
            for i in range(1, len(line), 4):
                if line[i].strip():
                    stacks[int(i / 4)].append(line[i])

        # Process movement
        if "move" in line:
            # move 3 from 1 to 2 => [[3], [1], [2]]
            line_split = line.split(" ")
            move = int(line_split[1])

            # -1 to convert to zero indexed list
            from_ = int(line_split[3]) - 1
            to = int(line_split[5]) - 1
            movements.append([move, from_, to])

    for index in range(len(stacks)):
        stacks[index].reverse()

    return (stacks, movements)


def part_1(data):
    solution = []

    stacks, movements = data

    for m in movements:
        for i in range(m[0]):
            if len(stacks[m[1]]) == 0:
                continue

            item = stacks[m[1]].pop(-1)
            stacks[m[2]].append(item)

    for stack in stacks:
        solution.append(stack[-1])

    return "".join(solution)


def part_2(data):
    solution = []

    stacks, movements = data

    for m in movements:
        # move 3 from 1 to 2 => [[3], [1], [2]]
        if len(stacks[m[1]]) == 0:
            continue

        stacks[m[2]].extend(stacks[m[1]][-m[0] :])
        stacks[m[1]] = stacks[m[1]][: -m[0]]

    for stack in stacks:
        solution.append(stack[-1])

    return "".join(solution)


def main():

    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    assert part_1(data_test) == "CMZ"
    assert part_1(data) == "GRTSWNJHH"

    # Reloading data
    # Because i couldn't be botherd to figure out why input data is alterd
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    assert part_2(data_test) == "MCD"
    assert part_2(data) == "QLFQDBBHM"

    # print(part_1(data_test))
    # print(part_1(data))
    # print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
