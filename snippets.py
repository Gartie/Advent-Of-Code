

int_list = [*map(int, "4 5 6 7 8 5".split())]
# [4, 5, 6, 7, 8, 5]


# Dataclasses
# Check 2023/02
# Check 2023/03
from dataclasses import dataclass
from typing import List

@dataclass
class Round:
    r: int = 0
    g: int = 0
    b: int = 0


@dataclass
class Game:
    id: int
    rounds: List[Round]
    
    
    
# 2d matrix 
# Check 2023/03

# Rotate 2d matrix
def rotate_ccw(li):
	return list(zip(*li))[::-1]
	
def rotate_cw(li):
    return list(zip(*li[::-1]))
# Rotate 2d matrix - END


# Load matrix with added border
def load_data(Path):
    data_list = []
    border_char = "#"
    with open(Path, "r") as file:
        [data_list.append(border_char + line.strip() + border_char) for line in file]

    data_list.insert(0, border_char * len(data_list[0]))
    data_list.append(border_char * len(data_list[0]))

    return data_list
# Load matrix with added border - END

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
