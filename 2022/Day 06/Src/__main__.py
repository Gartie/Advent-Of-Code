""" Day 06 of the 2022 Advent of Code
https://adventofcode.com/2022/day/6
https://adventofcode.com/2022/day/6/input """


def load_data(Path):
    data = ""
    with open(Path, "r") as file:
        data = file.read()
    return data


def part_x(data, length):
    if len(data) < length:
        raise Exception("Sorry, no solution found")

    lenght_minus = length - 1
    for index in range(lenght_minus, len(data)):
        subset = data[index - lenght_minus : index + 1]
        subset = set(subset)
        if len(subset) == length:
            return index + 1
    else:
        raise Exception("Sorry, no solution found")


def main():
    data = load_data("..//Data//Prod.txt")

    assert part_x("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert part_x("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert part_x("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert part_x("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11
    assert part_x(data, 4) == 1655

    assert part_x("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert part_x("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert part_x("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert part_x("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert part_x("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26
    assert part_x(data, 14) == 2665

    # print(part_x(data, 4))
    # print(part_x(data, 14))


if __name__ == "__main__":
    main()
