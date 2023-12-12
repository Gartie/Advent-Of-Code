''' Day 6 of the 2023 Advent of Code
https://adventofcode.com/2023/day/6
https://adventofcode.com/2023/day/6/input '''

def load_data(Path):
    data_list = []

    if "Prod" in Path:
        # Time:      48   93   84   66
        # Distance: 261 1192 1019 1063
        data_list = [
            [48, 261 ],
            [93, 1192],
            [84, 1019],
            [66, 1063]
        ]

    if "Test" in Path:
        data_list = [
            [7, 9],
            [15, 40],
            [30, 200]
        ]

    return data_list
    
    
def get_winning_count(time, record):
    race_value = 0
    
    for time_button in range(time+1):
        distance = time_button*(time-time_button)
        if distance > record:
            race_value += 1
    
    return race_value
    
    
def part_1(data):
    solution = 1

    for race in data:
        race_value = get_winning_count(race[0], race[1])
        solution *= race_value
    
    return solution

    
def part_2(data):
    time_str   = ""
    record_str = ""

    for race in data:
        time_str += str(race[0])
        record_str += str(race[1])
    
    solution = get_winning_count(int(time_str), int(record_str))
    return solution    


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    assert part_1(data_test) == 288
    assert part_1(data) == 1312850
    assert part_2(data_test) == 71503
    assert part_2(data) == 36749103
    
if __name__ == "__main__":
    main()
    
