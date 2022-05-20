''' Day 15 of the 2021 Advent of Code
https://adventofcode.com/2021/day/15
https://adventofcode.com/2021/day/15/input '''

def load_data(Path):
    data_list = []
    with open(Path, 'r') as file:
        [data_list.append(line.strip()) for line in file]
    return data_list

    
def part_1(data):
    solution = None    
    return solution

    
def part_2(data):
    solution = None
    return solution    


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    
    assert part_1(data_test) == None
    assert part_1(data) == None
    assert part_2(data_test) == None
    assert part_2(data) == None
    
    print(part_1(data_test))
    # print(part_1(data))
    print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
