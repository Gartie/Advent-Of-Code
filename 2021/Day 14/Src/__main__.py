''' Day 14 of the 2021 Advent of Code
https://adventofcode.com/2021/day/14
https://adventofcode.com/2021/day/14/input '''
from collections import namedtuple
from collections import Counter
from datetime import datetime
import re 

from dataclasses import dataclass


@dataclass
class Pair:
    char_pair: str
    target_pairs: []
    total_count: int = 0
    step_count: int = 0


def load_data(path):
    pairs = {}
    poly = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if " -> " in line:
                char_pair = line[:2]
                total_count = 0
                step_count = 0
                
                target = line[6:]
                target_values = []
                target_values.append( char_pair[0] + target )
                target_values.append( target + char_pair[1] )
                
                pairs[char_pair] = Pair(char_pair, target_values, total_count, step_count)
                continue

            poly = [c for c in line]
    for i in range(len(poly)):
        if i+1 == len(poly):
            continue
        
        char_pair = poly[i] + poly[i+1]
        pairs[char_pair].total_count += 1
    
    return pairs

        
def part_1(pairs, itterations=10):

    solution = None

    for char, data in pairs.items():
        print(char, data)
    print()
    
    for _ in range(itterations):
        # for pair in pairs:
        for _, pair in pairs.items():
            if pair.total_count == 0:
                continue
            
            for target_pair in pair.target_pairs:
                pairs[target_pair].step_count += pair.total_count
                
        for _, pair in pairs.items():
            pair.total_count += pair.step_count
            pair.step_count = 0
            
            
    for char, data in pairs.items():
        print(char, data)
    print()
    
    
    
    return solution

    

def main():
    pairs = load_data("..//Data//Prod.txt")
    pairs_test = load_data("..//Data//Test.txt")
    
    # print( part_1(poly_test, insertions_test, 40) )
    print( part_1(pairs_test, 10) )

    # assert part_1(poly_test, insertions_test, 10) == 1588
    # assert part_1(poly, insertions, 10) == 4517
    # assert part_1(poly_test, insertions_test, 40) == 2188189693529
    # assert part_1(poly, insertions, 10) == None


if __name__ == "__main__":
    main()


    # poly_counter = Counter(poly)
    # max_poly = poly_counter.most_common()[0][1]
    # mix_poly = poly_counter.most_common()[-1][1]
    # solution = max_poly - mix_poly
