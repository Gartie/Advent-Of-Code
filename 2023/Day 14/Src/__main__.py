''' Day 14 of the 2023 Advent of Code
https://adventofcode.com/2023/day/14
https://adventofcode.com/2023/day/14/input '''



def load_data(Path):
    data_list = []
    with open(Path, 'r') as file:
        [data_list.append([c for c in line.strip()]) for line in file]
    return data_list


def matrix_rotate_ccw(li):
    li = list(zip(*li))[::-1]
    li = ["".join(n) for n in li]
    return li
	
    
def matrix_rotate_cw(li):
    li = list(zip(*li[::-1]))
    li = ["".join(n) for n in li]
    return li


def sort_string(s):
    s = sorted(s, reverse=True)
    s = "".join(s)
    return s
    
    
def tilt_west(data):
    new_data = []
        
    for r in data:
        row = r.split("#")
        row = [sort_string(chunck) for chunck in row]
        row = "#".join(row)
        new_data.append(row) 
        
    return new_data


def tilt_north(data):
    data = matrix_rotate_ccw(data)
    data = tilt_west(data)
    data = matrix_rotate_cw(data)
    return data
    
    
def tilt_south(data):
    data = matrix_rotate_cw(data)
    data = tilt_west(data)
    data = matrix_rotate_ccw(data)
    return data
    
    
def tilt_east(data):
    data = matrix_rotate_ccw(data)
    data = matrix_rotate_ccw(data)
    data = tilt_west(data)
    data = matrix_rotate_cw(data)
    data = matrix_rotate_cw(data)
    return data

    
def tilt_cycle(data):
    data = matrix_rotate_ccw(data) # -1
    data = tilt_west(data)

    data = matrix_rotate_cw(data)  # 0
    data = tilt_west(data)

    data = matrix_rotate_cw(data)  # 1
    data = tilt_west(data)
    
    data = matrix_rotate_cw(data)  # 2
    data = tilt_west(data)

    data = matrix_rotate_ccw(data) # 1
    data = matrix_rotate_ccw(data) # 0
    
    return data
    
    
def load_north(data):
    load = 0
    
    for i, row in enumerate(data):
        rock_score = len(data) - i
        rock_count = len([i for i in row if i == "O"])
        load += rock_count*rock_score
    
    return load
    
    
def part_1(data):
    solution = None

    data = tilt_north(data)
    solution = load_north(data)
    
    return solution

    
def part_2(data):
    solution = None
    
    return solution    


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    
    assert part_1(data_test) == 136
    assert part_1(data) == 109596
    # assert part_2(data_test) == None
    # assert part_2(data) == None
    
    # print(part_1(data_test))
    # print(part_1(data))
    # print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
