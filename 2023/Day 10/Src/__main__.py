''' Day 10 of the 2023 Advent of Code
https://adventofcode.com/2023/day/10
https://adventofcode.com/2023/day/10/input '''

# 2d matrix Print
def get_martix_header_indexes(data_width, witch_header, padding):
    assert witch_header in [1, 10, 100, 1000]
    wh = witch_header
    header_list = []
    padding = str(padding)
    padding += " "*(wh-1) 

    if data_width < wh:
        return ""

    for i in range(wh-1, data_width):
        if wh == 1:
                header_list.append( int(i%10) )
        else:
            header_list.append( int(i/wh%wh) )

    header = "".join(map(str, header_list))
    header = padding + header
    return header

def print_matrix_header(data_width, padding_width):
    padding = " "*padding_width
    if data_width > 99:
        print(get_martix_header_indexes(data_width, 100, padding))
    if data_width > 9:
        print(get_martix_header_indexes(data_width, 10, padding))
    print(get_martix_header_indexes(data_width, 1, padding))
    print(padding + "-"*data_width, sep="")

    
def print_matrix(data):
    assert len(data) >= 0
    data_width = len(data[0])
    data_length = len(data)
    column_suffix = "| "
    padding_width = len(str(data_length))
    padding_width_total = padding_width+len(column_suffix)
    padding = " "*padding_width_total
    
    print_matrix_header(data_width, padding_width_total)

    [print(str(i).rjust(padding_width)+column_suffix, d, sep="") for i, d in enumerate(data)]
    print()
    print()
# 2d matrix Print - End

def load_data(Path):
    data_list = []
    with open(Path, 'r') as file:
        for line in file:
            line = line.strip()
            line = "." + line + "."
            data_list.append(line.strip()) 
            
    padding = "."*len(data_list[0])
    data_list.insert(0, padding)
    data_list.append(padding)
    
    return data_list

def starting_position(matrix):
    index_row = -1
    index_col = -1
    for i, row in enumerate(matrix):
        if "S" in row:
            index_row = i
            index_col = row.index("S")
    
    return (index_row, index_col)


def connected_neihgbours(matrix, pos):
    '''
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
    '''
    row, col = pos
    curr = matrix[row][col]
    char_n = matrix[row-1][col]
    char_s = matrix[row+1][col] 
    char_l = matrix[row][col-1] 
    char_r = matrix[row][col+1] 
    
    connections = []
    if char_n in "|7FS" and curr in "S|JL":
        connections.append( (row-1, col) )
    
    if char_s in "|LJS" and curr in "S|F7":
        connections.append( (row+1, col) )
    
    if char_l in "-LFS" and curr in "S-7J":
        connections.append( (row, col-1) )
        
    if char_r in "-7JS" and curr in "S-FL":
        connections.append( (row, col+1) )
    
    return connections
    
def next_segment(matrix, curr, last):
    next_pos = None
    
    connections = connected_neihgbours(matrix, curr)
    next_pos = [c for c in connections if not c == last]
    
    if not next_pos:
        raise RuntimeError(f"No connections found for {curr}, last was {last}")

    next_pos = next_pos[0]
    return next_pos
    
    
def part_1(data):
    solution = None
    position_count = 1
    
    pos_start = starting_position(data)
    curr_pos = next_segment(data, pos_start, (-1, -1))
    last_pos = pos_start
    
    while not curr_pos == pos_start:
        position_count += 1
        next_pos = next_segment(data, curr_pos, last_pos)
        last_pos = curr_pos
        curr_pos = next_pos
    
    solution = int( position_count/2 )
    return solution

    
def part_2(data):
    solution = None
    position_count = 1
    
    all_pos = []
    pos_start = starting_position(data)
    curr_pos = next_segment(data, pos_start, (-1, -1))
    last_pos = pos_start
    
    while not curr_pos == pos_start:
        position_count += 1
        next_pos = next_segment(data, curr_pos, last_pos)
        last_pos = curr_pos
        curr_pos = next_pos
        all_pos.append(curr_pos)
        
    
    for r, c in all_pos[0:1:1]:
        data[r] = data[r][:c-1:] + "X" + data[r][c::]
    print_matrix(data)
    
    return solution  


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    
    assert part_1(data_test) == 8
    assert part_1(data) == 6725
    # assert part_2(data_test) == None
    # assert part_2(data) == None
    
    # print(part_2(data_test))
    print(part_2(data))


if __name__ == "__main__":
    main()

'''
# test data
# Part 1 = 4
.....
.S-7.
.|.|.
.L-J.
.....

'''
'''
# test data, iets lastiger
# Part 1 = 8
..F7.
.FJ|.
SJ.L7
|F--J
LJ...

'''