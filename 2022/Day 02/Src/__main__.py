''' Day 02 of the 2022 Advent of Code
https://adventofcode.com/2022/day/2
https://adventofcode.com/2022/day/2/input '''

def load_data(Path):
    data_list = []
    
    with open(Path, 'r') as raw_file:
        file = raw_file.read()
 
    file = file.replace("A", "1")
    file = file.replace("B", "2")
    file = file.replace("C", "3")

    file = file.replace("X", "1")
    file = file.replace("Y", "2")
    file = file.replace("Z", "3")

    lines = file.split("\n")
    
    for line in lines:
        y, z = line.split(" ")
        y = int(y)
        z = int(z)
        data_list.append([y, z])
           
           
    return data_list


def get_score_part_1(you, opp):

    if (you == 1 and opp == 3) or \
       (you == 3 and opp == 2) or \
       (you == 2 and opp == 1):
        return 6 + you
 
    if you == opp:
        return 3 + you

    return you

    
def get_score_part_2(you, opp):

    # Lose    
    if you == 1:
        if opp == 1: return 0 + 3
        if opp == 2: return 0 + 1
        if opp == 3: return 0 + 2
        
    # Win
    if you == 3:
        if opp == 1: return 6 + 2
        if opp == 2: return 6 + 3
        if opp == 3: return 6 + 1

    # Draw
    return 3 + opp
    

    
def part_1(data):
    score = 0

    for a, b in data:
        score = score + get_score_part_1(b, a)

    return score

    
def part_2(data):
    score = 0

    for a, b in data:
        score = score + get_score_part_2(b, a)

    return score    


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    
    assert part_1(data_test) == 15
    assert part_1(data) == 12586
    assert part_2(data_test) == 12
    assert part_2(data) == 13193
    
    # print(part_1(data_test))
    # print(part_1(data))
    # print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
