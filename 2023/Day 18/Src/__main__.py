''' Day 18 of the 2023 Advent of Code
https://adventofcode.com/2023/day/18
https://adventofcode.com/2023/day/18/input '''
from collections import namedtuple

Instruction = namedtuple("Instruction", ["direction", "distance", "color"])
Point = namedtuple("Point", ["r", "c"])


def load_data(Path):
    data_list = []
    with open(Path, 'r') as file:
        
        for line in file:
            line = line.strip()
            
            if not line:
                continue
                
            direction, dis, col = line.split()
            dis = int(dis)
            col = col[1:8:]
            
            instr = Instruction(direction, dis, col)
            data_list.append(instr)
        
    return data_list


def hole_dimention(data, plus_op, min_op):
    curr_max = 0
    curr = 0
    for d in data:
        if d.direction == plus_op:
            curr += d.distance
        if d.direction == min_op:
            curr -= d.distance
        curr_max = max(curr_max, curr)
    
    curr_max += 1
    return curr_max


def hole_size(data):
    max_d = hole_dimention(data, "D", "U")
    max_u = hole_dimention(data, "U", "D")
    max_r = hole_dimention(data, "R", "L")
    max_l = hole_dimention(data, "L", "R")
    
    return (max_l, max_r, max_u, max_d)


def create_matrix(height, width):
    matrix = [["." for _ in range(width)] for _ in range(height)]
    return matrix


def count_hex(matrix):
    count = 0
    for row in matrix:
        for col in row:
            if col in "#.":
                count += 1

    return count

    
def matrix_to_file(matrix, filename=""):
    if not filename:
        filename = "out.txt"
    with open(filename, "w") as file:
        for row in matrix:
            file.write("".join(row) + "\n")

def matrix_flood_fill(matrix):
    points = []
    start = Point(0, 0)
    points.append(start)

    while points:
        point = points.pop()
        
        # print(size, point)
        if not matrix[point.r][point.c] == ".":
            continue
        
        matrix[point.r][point.c] = "X"
        
        if point.r > 0:
            # if matrix[point.r-1][point.c] == "."
            points.append(Point(point.r-1, point.c))
            
        if point.r < len(matrix)-1:
            # if matrix[point.r+1][point.c] == "."
            points.append(Point(point.r+1, point.c))
        
        if point.c > 0:
            # if matrix[point.r][point.c-1] == "."
            points.append(Point(point.r, point.c-1))
        
        if point.c < len(matrix[0])-1:
            # if matrix[point.r][point.c+1] == "."
            points.append(Point(point.r, point.c+1))
            
    return matrix

  
def part_1(data):
    solution = None    
    
    max_l, max_r, max_u, max_d = hole_size(data)

    height = max_u + max_d + 1
    width  = max_l + max_r + 1

    print(height, width)
    matrix = create_matrix(height, width)
    print("matrix created")
    curr_r = max_u
    curr_c = max_l
    matrix[curr_r][curr_c] = "#"
    
    
    for ins in data:
        print(ins)
        for _ in range(ins.distance):
            if ins.direction == "R":
                curr_c += 1
            elif ins.direction == "L":
                curr_c -= 1
            elif ins.direction == "U":
                curr_r -= 1
            elif ins.direction == "D":
                curr_r += 1
            
            matrix[curr_r][curr_c] = "#"
    print("intructions finished")
    matrix = matrix_flood_fill(matrix)
    print("fluif fill finished")
    # matrix_to_file(matrix)
    solution = count_hex(matrix)
    return solution

    
def part_2(data):
    solution = None
    # new_data = []
    # directions = "RDLU"
    # for d in data:
        # direction = int(d.color[6:])
        # direction = directions[direction]
        # dis = int(d.color[1:6:] , base=16)
        # col = d.color
        
        # instr = Instruction(direction, dis, col)
        # new_data.append(instr)
    # print("#"*40)
    # print("#"*40)
    # print("#"*40)
    # solution = part_1(new_data)

    # [print(d) for d in new_data]
    
    return solution    


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    
    # assert part_1(data_test) == 62
    # assert part_1(data) == 28911
    # assert part_2(data_test) == None
    # assert part_2(data) == None
    
    # print(part_1(data_test))
    # print(part_1(data))
    print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
