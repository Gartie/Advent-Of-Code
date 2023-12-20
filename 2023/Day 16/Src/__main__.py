''' Day 16 of the 2023 Advent of Code
https://adventofcode.com/2023/day/16
https://adventofcode.com/2023/day/16/input '''
from collections import namedtuple

Beam = namedtuple("Beam", ["r", "c", "direction"])

def load_data(Path):
    data_list = []
    char = "#"
    with open(Path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            line = char + line + char
            data_list.append(line)

    data_list.insert(0, char * len(data_list[0]))
    data_list.append(char * len(data_list[0]))

    return data_list


def beam_to_str(beam):
    return f"{beam.r}-{beam.c}-{beam.direction}"


def beam_next_step(char, direction):
    directions = ""
    if (direction == "R" and char in "-.") or \
       (direction == "D" and char in "-\\") or \
       (direction == "U" and char in "-/"):
        # add right
        directions += "R"

    if (direction == "L" and char in "-.") or \
       (direction == "D" and char in "-/") or \
       (direction == "U" and char in "-\\"):
        # add right
        directions += "L"

    if (direction == "U" and char in "|.") or \
       (direction == "L" and char in "|\\") or \
       (direction == "R" and char in "|/"):
        # add up
        directions += "U"

    if (direction == "D" and char in "|.") or \
       (direction == "L" and char in "|/") or \
       (direction == "R" and char in "|\\"):
        # add down
        directions += "D"

    return directions


def trace_ray_poor_ray(data, starting_beam):
    seen_tiles = set()
    beams = []
    beams.append(starting_beam)

    while beams:
        new_beams = []

        for beam in beams:
            char = data[beam.r][beam.c]
            beam_str = beam_to_str(beam)

            if char == "#":
                # Out of bounds, beam ends
                continue

            if beam_str in seen_tiles:
                # position and direction already seen, skip to prevent loops
                continue

            seen_tiles.add(beam_str)
            directions = beam_next_step(char, beam.direction)

            if "U" in directions:
                new_beams.append(Beam(beam.r-1, beam.c, "U"))
            if "D" in directions:
                new_beams.append(Beam(beam.r+1, beam.c, "D"))
            if "L" in directions:
                new_beams.append(Beam(beam.r, beam.c-1, "L"))
            if "R" in directions:
                new_beams.append(Beam(beam.r, beam.c+1, "R"))

        beams = new_beams.copy()

    sol_set = set()
    for tile in seen_tiles:
        r, c, _ = tile.split("-")
        sol_set.add(r + "-" + c)

    solution = len(sol_set)
    return solution


def part_1(data):
    solution = None
    starting_beam = Beam(1, 1, "R")
    solution = trace_ray_poor_ray(data, starting_beam)
    return solution


def part_2(data):
    solution = None
    starting_points = []

    size = len(data)
    for r in range(size):
        full_row = (r == 1 or r == size-2)
        for c in range(size):
            edge = (full_row or c == size-2 or c == 1)
            if not edge:
                continue

            if r == 1:
                starting_points.append(Beam(r, c, "D"))
            if r == size-2:
                starting_points.append(Beam(r, c, "U"))

        starting_points.append(Beam(r,      1, "R"))
        starting_points.append(Beam(r, size-2, "L"))

    solution_values = []
    for i, sp in enumerate(starting_points):
        sp_value = trace_ray_poor_ray(data, sp)
        solution_values.append(sp_value)

    solution = max(solution_values)
    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 46
    assert part_1(data) == 7434
    assert part_2(data_test) == 51
    assert part_2(data) == 8183


if __name__ == "__main__":
    main()
