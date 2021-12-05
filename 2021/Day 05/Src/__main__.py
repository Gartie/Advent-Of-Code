""" Day 05 of the 2021 Advent of Code
https://adventofcode.com/2021/day/05
https://adventofcode.com/2021/day/05/input
Cool, a dataclass!"""

from dataclasses import dataclass
import numpy as np


@dataclass
class VentLine:
    """Class for storing Hydrothermal vent_line data.
    The coordinates are zero-indexed!"""

    x_start: int
    x_end: int
    y_start: int
    y_end: int

    def is_diagonal(self):
        y_dif = abs(self.y_start - self.y_end)
        x_dif = abs(self.x_start - self.x_end)
        return y_dif == x_dif

    def is_horizontal(self):
        return self.y_start == self.y_end

    def is_vertical(self):
        return self.x_start == self.x_end


def load_data(path):
    """Parses an file with input data, returns a list of class vent_line() objects.
    '20,136 -> 819,935\n' ==> vent_line(x_start=20, x_end=136, y_start=819, y_end=935)"""

    data_list = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            x_full, y_full = line.split(" -> ")
            x_start, y_start = x_full.split(",")
            x_end, y_end = y_full.split(",")
            x_start, x_end, y_start, y_end = (
                int(x_start),
                int(x_end),
                int(y_start),
                int(y_end),
            )
            data_list.append(VentLine(x_start, x_end, y_start, y_end))

    return data_list


def mark_grid(grid, vent_lines, do_diagonals=False):

    if len(vent_lines) == 0:
        return grid

    vent_line = vent_lines[0]
    is_horizontal = vent_line.is_horizontal()
    x_start = vent_line.x_start
    x_end = vent_line.x_end
    y_start = vent_line.y_start
    y_end = vent_line.y_end

    # Mark vertical lines
    # Single point lines are marked here.
    if is_horizontal:

        # draw left to right
        if x_start > x_end:
            x_start, x_end = x_end, x_start
            y_start, y_end = y_end, y_start

        for i in range(line_start, line_end + 1):
            grid[y_start][i] += 1

    # Mark vertical lines
    # check is_horizontal to prevent single point lines from being marked more than once.
    if vent_line.is_vertical() and not is_horizontal:

        # draw top to bottom
        if y_start > y_end:
            x_start, x_end = x_end, x_start
            y_start, y_end = y_end, y_start

        for i in range(y_start, y_end + 1):
            grid[i][x_start] += 1

    # Mark diagonals line
    # check is_horizontal to prevent single point lines from being marked more than once.
    if do_diagonals and vent_line.is_diagonal() and not is_horizontal:

        # draw from top to bottom
        if y_start > y_end:
            x_start, x_end = x_end, x_start
            y_start, y_end = y_end, y_start

        length_on_axis = abs(y_start - y_end) + 1

        for i in range(length_on_axis):
            y_pos = y_start + i
            x_pos = x_start + i

            if x_start > x_end:
                x_pos = x_start + (0 - i)

            grid[y_pos][x_pos] += 1

    return mark_grid(grid, vent_lines[1:], do_diagonals)


def part_1(vent_lines, grid_size, do_diagonals=False):
    grid = np.zeros((grid_size, grid_size))
    grid = mark_grid(grid, vent_lines, do_diagonals)
    solution = (grid >= 2).sum()
    return solution


def part_2(vent_lines, grid_size):
    solution = part_1(vent_lines, grid_size, do_diagonals=True)
    return solution


def main():
    grid_size = 1000
    grid_size_test = 10
    vent_lines = load_data("..//Data//Prod.txt")
    vent_lines_test = load_data("..//Data//Test.txt")

    assert part_1(vent_lines_test, grid_size_test) == 5
    assert part_1(vent_lines, grid_size) == 5124
    assert part_2(vent_lines_test, grid_size_test) == 12
    assert part_2(vent_lines, grid_size) == 19771


if __name__ == "__main__":
    main()
