''' Day 8 of the 2023 Advent of Code
https://adventofcode.com/2023/day/8
https://adventofcode.com/2023/day/8/input '''
import math

def load_data(Path):
    instructions = []
    nodes = {}
    with open(Path, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            elif "=" in line:
                name  = line[:3:]
                left  = line[7:10:]
                right = line[12:15:]
                nodes[name] = [left, right]
            else:
                instructions = [int(char=="R") for char in line.strip()]
                
    return (instructions, nodes)


def check_AAA(node):
    return node == "ZZZ"
    
    
def check_last_Z(node):
    return node.endswith("Z")
    

def get_solution(node, data, check_function):
    instructions = data[0]
    nodes        = data[1]
    solution = 0
    found = False
    while not found:
        for i in instructions:
            solution += 1
            node = nodes[node][i]
            if check_function(node):
                found = True
                return solution
        
        
def part_1(data):
    solution = get_solution("AAA", data, check_AAA)
    return solution


def part_2(data):
    solution = 1
    instructions = data[0]
    nodes        = data[1]
    starting_nodes = [n for n in nodes if n.endswith("A")]

    for node in starting_nodes:
        curr_solution = get_solution(node, data, check_last_Z)
        solution = math.lcm(curr_solution, solution)

    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert part_1(data_test) == 6
    assert part_1(data) == 11911
    assert part_2(data_test) == 6
    assert part_2(data) == 10151663816849


if __name__ == "__main__":
    main()
