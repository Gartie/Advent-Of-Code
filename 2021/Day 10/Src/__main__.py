""" Day 10 of the 2021 Advent of Code
https://adventofcode.com/2021/day/10
https://adventofcode.com/2021/day/10/input """


def load_data(path):
    data_list = []

    with open(path, "r") as file:
        for line in file:
            data_list.append(line.strip())

    return data_list


def get_corrupt_char_in_line(line):
    seen_values = [line[0]]
    line = line[1:]
    ref_chars = [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]

    for char in line:
        if char in ("(", "[", "{", "<"):
            seen_values.append(char)
            continue

        for ref_char in ref_chars:
            if char == ref_char[1]:
                if seen_values[-1] == ref_char[0]:
                    seen_values.pop(-1)
                    continue
                return char

    return seen_values


def part_1(data):
    solution = 0

    for line in data:
        char = get_corrupt_char_in_line(line)
        if len(char) > 1:
            continue

        if char == ")":
            solution += 3
            continue

        if char == "]":
            solution += 57
            continue

        if char == "}":
            solution += 1197
            continue

        if char == ">":
            solution += 25137
            continue

    return solution


def part_2(data):
    solution = None
    score_list = []

    for line in data:
        local_score = 0
        ref_values = [None, "(", "[", "{", "<"]

        chars = get_corrupt_char_in_line(line)

        if len(chars) == 1:
            continue

        chars.reverse()
        for char in chars:
            local_score *= 5
            local_score += ref_values.index(char)

        score_list.append(local_score)

    score_list.sort()
    solution = score_list[int(len(score_list) / 2)]

    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert get_corrupt_char_in_line("{([(<{}[<>[]}>{[]{[(<()>") == "}"
    assert get_corrupt_char_in_line("[[<[([]))<([[{}[[()]]]") == ")"
    assert get_corrupt_char_in_line("[{[{({}]{}}([{[{{{}}([]") == "]"
    assert get_corrupt_char_in_line("[<(<(<(<{}))><([]([]()") == ")"
    assert get_corrupt_char_in_line("<{([([[(<>()){}]>(<<{{") == ">"
    assert get_corrupt_char_in_line("{([(<{}[<>[]}>{[]{[(<()>") == "}"

    assert part_1(data_test) == 26397
    assert part_1(data) == 392139
    assert part_2(data_test) == 288957
    assert part_2(data) == 4001832844


if __name__ == "__main__":
    main()
