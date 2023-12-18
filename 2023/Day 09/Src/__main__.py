''' Day 9 of the 2023 Advent of Code
https://adventofcode.com/2023/day/9
https://adventofcode.com/2023/day/9/input '''


def load_data(Path):
    data_list = []
    with open(Path, 'r') as file:
        for line in file:
            line = line.strip()
            line = line.split()
            int_list = [*map(int, line)]
            data_list.append(int_list)
   
    return data_list


def predict_next_value(his):
    last_values = []
    last_values.append(his[-1])
    while his and any(his):
        his = [his[i+1]-his[i] for i in range(0,len(his)-1)]
        if not his:
            break
        last_values.append(his[-1])

    next_value = 0
    for value in last_values[::-1]:
        next_value += value
        
    return next_value
    

def part_1(data):
    solution = 0    

    for his in data:
        solution += predict_next_value(his)
        
    return solution
    
    
def part_2(data):
    solution = 0    
    
    for his in data:
        his.reverse()
        solution += predict_next_value(his)
        
    return solution  


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    
    assert part_1(data_test) == 114
    assert part_1(data) == 1930746032
    assert part_2(data_test) == 2
    assert part_2(data) == 1154
    

if __name__ == "__main__":
    main()
