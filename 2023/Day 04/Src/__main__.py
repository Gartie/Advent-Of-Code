''' Day 4 of the 2023 Advent of Code
https://adventofcode.com/2023/day/4
https://adventofcode.com/2023/day/4/input
'''
from dataclasses import dataclass
from typing import List


@dataclass
class ScratchCard:
    id: int
    winning_numbers: List[int]
    numbers_you_have: List[int]
    overlap: int = 0
    
    def __post_init__(self):
        self.overlap = len( set(self.winning_numbers) & set(self.numbers_you_have) )
    

def load_data(Path):
    data_list = []
    with open(Path, 'r') as file:
        for line in file:
            id, line = line.split(":")
            id = int(id.split()[1])
            winning_numbers, numbers_you_have = line.split("|")
            winning_numbers = [*map(int, winning_numbers.split())]
            numbers_you_have = [*map(int, numbers_you_have.split())]
            data_list.append(ScratchCard(id, winning_numbers, numbers_you_have))
            
    return data_list

    
def part_1(data):
    solution = 0    
    for card in data:
        solution += bool(card.overlap)*2**(card.overlap-1)
        
    return solution

    
def part_2(data):
    solution = None
    
    # list of ints, default value is 1 because we have the original cards
    count_list = [1,]*len(data)
    
    for card_index, card in enumerate(data):
        for win in range(card.overlap):
            if card_index + win + 1 < len(count_list):
                count_list[card_index+win+1] += count_list[card_index]
        
    solution = sum(count_list)    
    
    return solution    


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    
    assert part_1(data_test) == 13
    assert part_1(data) == 22674
    assert part_2(data_test) == 30
    assert part_2(data) == 5747443
    

if __name__ == "__main__":
    main()
