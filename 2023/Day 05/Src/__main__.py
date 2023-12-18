''' Day 5 of the 2023 Advent of Code
https://adventofcode.com/2023/day/5
https://adventofcode.com/2023/day/5/input '''

def line_to_int_list(line):
    int_list = [*map(int, line.split())]
    return int_list

def load_data(Path):
    data_list = []
    seeds = []
    with open(Path, 'r') as file:
        step_values = []
        for line in file:
            if "seeds:" in line:
                line = line.replace("seeds:", "")
                seeds = line_to_int_list(line)
                continue
                
            elif ":" in line:
                continue
                
            elif line.strip() == "":
                if step_values:
                    data_list.append(step_values)
                step_values = []
                continue
                
            else:
                step_values.append(line_to_int_list(line))
    
        if step_values:
            data_list.append(step_values)

    return (seeds, data_list)

def run_trough_maps(seed, maps):
    for cur_map in maps:
        for dest, source, rang in cur_map:
            if seed >= source and seed < source+rang:
                seed = seed + (dest - source)
                break
    return seed
    
    
def part_1(data):
    solution = None
    seeds, maps = data
    locations = []

    for seed in seeds:
        seed = run_trough_maps(seed, maps)
        locations.append(seed)

    solution = min(locations)
    
    return solution

    
def part_2(data):
    solution = None
    seeds, maps = data
    locations = []
    for i in range(0, len(seeds), 2):
        for seed in range(seeds[i], seeds[i]+seeds[i+1]):
            seed = run_trough_maps(seed, maps)
            locations.append(seed)

    solution = min(locations)

    return solution    


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    
    assert part_1(data_test) == 35
    assert part_1(data) == 993500720
    assert part_2(data_test) == 46
    # assert part_2(data) == None
    
    # print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
