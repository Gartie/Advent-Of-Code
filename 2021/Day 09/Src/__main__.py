""" Day 09 of the 2021 Advent of Code
https://adventofcode.com/2021/day/09
https://adventofcode.com/2021/day/09/input """

from dataclasses import dataclass
import math

#
@dataclass
class Location:
    """Class for keeping track of Locations."""

    line_index: int
    char_index: int
    value: int = -1


#
def load_data(Path):
    data_list = []
    with open(Path, "r") as file:
        for line in file:
            data_list.append(line.strip())
    return data_list


def is_part_of_plateau(center, left, right, above, below):
    if center in (left, right, above, below):
        return True
    return False


def is_lowspot(center, left, right, above, below):
    if center > left or center > right or center > above or center > below:
        return False

    return True


def locations_unique(location_list):
    unique = []

    for loc in location_list:
        if not location_in_locations(unique, loc):
            unique.append(loc)

    return unique


def location_in_locations(loc_list, location):

    if len(loc_list) == 0:
        return False

    for loc in loc_list:
        if loc.line_index == location.line_index:
            if loc.char_index == location.char_index:
                return True

    return False


def find_all_lowspots(data):
    lowspots = []
    for l, line in enumerate(data):
        for c, char in enumerate(line):
            center = int(char)

            left = 100
            if c > 0:
                left = line[c - 1]
                left = int(left)

            right = 100
            if c < len(line) - 1:
                right = line[c + 1]
                right = int(right)

            above = 100
            if l > 0:
                above = data[l - 1][c]
                above = int(above)

            below = 100
            if l < len(data) - 1:
                below = data[l + 1][c]
                below = int(below)

            if is_lowspot(center, left, right, above, below):
                if not is_part_of_plateau(center, left, right, above, below):
                    lowspots.append(Location(l, c, center))

    return lowspots


def part_1(data):
    solution = 0
    lowspots = find_all_lowspots(data)

    for ls in lowspots:
        char = data[ls.line_index][ls.char_index]
        solution += int(char) + 1

    return solution


def get_surrounding_spots(data, spot, boundary=9):
    found_spots = []

    c = spot.char_index
    l = spot.line_index
    line = data[l]

    if c > 0:
        left = int(line[c - 1])
        if left != boundary:
            found_spots.append(Location(l, c - 1, left))

    if c < len(line) - 1:
        right = int(line[c + 1])
        if right != boundary:
            found_spots.append(Location(l, c + 1, right))

    if l > 0:
        above = int(data[l - 1][c])
        if above != boundary:
            found_spots.append(Location(l - 1, c, above))

    if l < len(data) - 1:
        below = int(data[l + 1][c])
        if below != boundary:
            found_spots.append(Location(l + 1, c, below))

    found_spots = locations_unique(found_spots)
    return found_spots


def get_basin_size(data, location):
    spots_to_check = [location]
    location_spots = [location]
    while len(spots_to_check) > 0:
        spot = spots_to_check[0]
        spots_to_check = spots_to_check[1:]

        surr = get_surrounding_spots(data, spot)

        for spot in surr:
            if not location_in_locations(location_spots, spot):
                location_spots.append(spot)
                spots_to_check.append(spot)

    return len(location_spots)


def part_2(data):
    solution = None
    lowspots = find_all_lowspots(data)

    basin_sizes = []
    for location in lowspots:
        basin_sizes.append(get_basin_size(data, location))

    basin_sizes.sort(reverse=True)
    solution = math.prod(basin_sizes[:3])

    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 15
    assert part_1(data) == 508
    assert part_2(data_test) == 1134
    assert part_2(data) == 1564640


if __name__ == "__main__":
    main()
