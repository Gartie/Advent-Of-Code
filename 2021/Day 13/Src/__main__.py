""" Day 13 of the 2021 Advent of Code
https://adventofcode.com/2021/day/13
https://adventofcode.com/2021/day/13/input """
from collections import namedtuple


Dot = namedtuple("Dot", "right down")


def load_data(path):
    data_list = set()
    fold_list = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if "fold" in line:
                fold_list.append((line[11], int(line[13:])))
                continue

            if "," in line:
                right, down = line.split(",")
                data_list.add(Dot(int(right), int(down)))
                continue

    return data_list, fold_list


def fold_paper(data, folds, max_folds=0):
    fold_count = 0
    for fold, fold_pos in folds:
        if fold_count >= max_folds and max_folds:
            break
        fold_count += 1

        folded_cors = set()
        for cor in data:

            # Y ==> onder over boven, down wordt korter
            if fold == "y":
                # Dot is on the fold line
                if cor.down == fold_pos:
                    continue

                if cor.down < fold_pos:
                    folded_cors.add(cor)
                    continue

                new_down = (fold_pos * 2) - cor.down
                folded_cors.add(Dot(cor.right, new_down))
                continue

            # X ==> right over links, right wordt korter
            if fold == "x":
                # Dot is on the fold line
                if cor.right == fold_pos:
                    continue

                if cor.right < fold_pos:
                    folded_cors.add(cor)
                    continue

                new_right = (fold_pos * 2) - cor.right
                folded_cors.add(Dot(new_right, cor.down))
                continue

        data = folded_cors

    return data


def part_1(data, folds):
    solution = fold_paper(data, folds, max_folds=1)
    solution = len(solution)
    return solution


def part_2(data, folds):
    data = fold_paper(data, folds, max_folds=0)

    display = [["-"] * 40 for _ in range(6)]

    for cor in data:
        display[cor.down][cor.right] = "#"

    solution = ["".join(i) for i in display]
    solution = "\n".join(solution)
    return solution


def main():
    data, folds = load_data("..//Data//Prod.txt")
    test_data, test_folds = load_data("..//Data//Test.txt")

    # Part 1 only requers one fold. Skiped that while reading; did cost me hours :(
    assert part_1(test_data, test_folds) == 17
    assert part_1(data, folds) == 781

    assert part_2(test_data, test_folds) == "#####-----------------------------------\n#---#-----------------------------------\n#---#-----------------------------------\n#---#-----------------------------------\n#####-----------------------------------\n----------------------------------------"
    assert part_2(data, folds) == "###--####-###---##---##----##-###--###--\n#--#-#----#--#-#--#-#--#----#-#--#-#--#-\n#--#-###--#--#-#----#-------#-#--#-###--\n###--#----###--#----#-##----#-###--#--#-\n#----#----#-#--#--#-#--#-#--#-#----#--#-\n#----####-#--#--##---###--##--#----###--"


if __name__ == "__main__":
    main()