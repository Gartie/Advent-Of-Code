""" Day 12 of the 2021 Advent of Code
https://adventofcode.com/2021/day/12
https://adventofcode.com/2021/day/12/input """
from collections import namedtuple


Node = namedtuple("Node", "name is_small neighbours")


class CaveSystem:
    def create_nodes(self, connections):
        for node_1, node_2 in connections:
            if not node_1 in self.node_aliases:
                self.nodes.append(Node(node_1, node_1.islower(), []))
                self.node_aliases.append(node_1)

            if not node_2 in self.node_aliases:
                self.nodes.append(Node(node_2, node_2.islower(), []))
                self.node_aliases.append(node_2)

            alias_1 = self.node_aliases.index(node_1)
            alias_2 = self.node_aliases.index(node_2)

            self.nodes[alias_1].neighbours.append(alias_2)
            self.nodes[alias_2].neighbours.append(alias_1)

    def check_one_cave_aready_twice(self, path):
        for node_idx in path:
            if self.nodes[node_idx].is_small and path.count(node_idx) > 1:
                return False
        return True

    def check_all_possible_paths(self, one_small_cave_twice):
        active_paths = []
        active_paths.append([self.start_node_idx])

        while len(active_paths) > 0:
            path = active_paths[0]
            active_paths = active_paths[1:]

            for neighbor_inx in self.nodes[path[-1]].neighbours:

                if neighbor_inx == self.start_node_idx:
                    continue

                neighbor_count = path.count(neighbor_inx)
                if (
                    self.nodes[neighbor_inx].is_small
                    and neighbor_count
                    and neighbor_inx != self.end_node_idx
                ):
                    if not one_small_cave_twice:
                        continue

                    if neighbor_count >= 2:
                        continue

                    if not self.check_one_cave_aready_twice(path):
                        continue

                if neighbor_inx == self.end_node_idx:
                    self.paths_count += 1
                    continue

                new_path = path.copy()
                new_path.append(neighbor_inx)

                active_paths.append(new_path)

    def __init__(self, connections):
        self.nodes = []  # findable by index, witch is the same as the alias indec
        self.node_aliases = []  # index is alias, doubles as seen nodes
        self.create_nodes(connections)
        self.paths_count = 0
        self.start_node_idx = self.node_aliases.index("start")
        self.end_node_idx = self.node_aliases.index("end")


def load_data(path):
    data_list = []
    split_value = "-"
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            val_a, val_b = line.split(split_value)
            data_list.append((val_a, val_b))

    return data_list


def part_1(data):
    cave = CaveSystem(data)
    cave.check_all_possible_paths(one_small_cave_twice=False)
    return cave.paths_count


def part_2(data):
    cave = CaveSystem(data)
    cave.check_all_possible_paths(one_small_cave_twice=True)
    return cave.paths_count


def main():
    data = load_data("..//Data//Prod.txt")
    data_test_10 = load_data("..//Data//Test_10.txt")
    data_test_19 = load_data("..//Data//Test_19.txt")
    data_test_226 = load_data("..//Data//Test_226.txt")

    assert part_1(data_test_10) == 10
    assert part_1(data_test_19) == 19
    assert part_1(data_test_226) == 226
    assert part_1(data) == 3802

    assert part_2(data_test_10) == 36
    assert part_2(data_test_19) == 103
    assert part_2(data_test_226) == 3509
    # assert part_2(data) == 99448


if __name__ == "__main__":
    main()
