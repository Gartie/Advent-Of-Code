""" Day 07 of the 2022 Advent of Code
https://adventofcode.com/2022/day/7
https://adventofcode.com/2022/day/7/input """


from dataclasses import dataclass, field


@dataclass
class TreeNode:
    name: str
    parent: None
    children: list[None] = field(repr=False, default_factory=lambda: [])
    files: list[int] = field(repr=False, default_factory=lambda: [])

    def add_child(self, name):
        self.children.append(TreeNode(name, self))

    def add_file(self, file_size):
        self.files.append(file_size)

    def get_total_filesize(self):
        return sum(self.files)

    def get_child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return child
        else:
            return False

    def check_child_by_name(self, name):
        for child in self.children:
            if child.name == name:
                return true
        else:
            return False

    def print_self(self):
        print(self.name)
        for child in self.children:
            child.print_self()

    def sum_files(self, int):
        for child in self.children:
            int = child.sum_files(int)
        return int + sum(self.files)

    def sum_files_list(self, int_list=[]):
        for child in self.children:
            int_list.append(child.sum_files())
            child.sum_files_list(int_list)

        return int_list


def create_tree(data):
    root_node = TreeNode("/", None)
    current_node = root_node

    for line in data:
        if line == "$ ls":
            continue

        elif "$ cd " in line:
            name = line[5:]

            if name == "/":
                current_node = root_node
            elif name == "..":
                current_node = current_node.parent

            else:
                current_node = current_node.get_child_by_name(name)

        elif "dir " in line:
            name = line[4:]
            if not current_node.check_child_by_name(name):
                current_node.add_child(name)

        else:
            size = line.split(" ")[0]
            size = int(size)
            current_node.add_file(size)
    return root_node


def load_data(Path):
    data_list = []
    with open(Path, "r") as file:
        data_list = file.read().split("\n")
    data_list = [line.strip() for line in data_list]
    return data_list


def part_1(data):
    solution = None

    root_node = create_tree(data)

    solution = sum([i for i in root_node.sum_files_list([]) if i < 100000])

    return solution


def part_2(data):
    solution = None
    root_node = create_tree(data)
    int_list = root_node.sum_files_list([])

    curr_used_mem = root_node.sum_files(0)
    needed = 30000000 - (70000000 - curr_used_mem)

    for i in sorted(int_list):
        if i >= needed:
            solution = i
            break
    
    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 95437
    assert part_1(data) == 1350966
    assert part_2(data_test) == 24933642
    assert part_2(data) == 6296435

    # print(part_1(data_test))
    # print(part_1(data))
    # print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
