''' Day 14 of the 2021 Advent of Code
https://adventofcode.com/2021/day/14
https://adventofcode.com/2021/day/14/input '''
from collections import namedtuple
from collections import Counter
from datetime import datetime
import re 

PairInsertion = namedtuple("PairInsertion", "pair val")
InsertOrder = namedtuple("InsertOrder", "pos val")

def load_data(path):
    insertions = []
    poly_template = ''
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            if " -> " in line:
                insertions.append(PairInsertion(line[:2], line[6:]))
                continue

            poly_template = line
            
    return poly_template, insertions

def insert(string, char, pos):
    # "0123456789"[:5] == "01234" | "0123456789"[5:] == "56789"
    split_1 = string[:pos]
    split_2 = string[pos:]
    return ''.join([split_1 , char, split_2])

def return_InsertOrder_Pos(insert_order):
    return insert_order.pos

def get_insert_commands_1(string, insertions):
    commands = []
    
    for ins in insertions:
        for match in re.finditer(ins.pair, string):
            print(match)
            commands.append( InsertOrder(match.start()+1, ins.val) )

    commands.sort(reverse=True, key=return_InsertOrder_Pos)
    return commands


def get_insert_commands(string, insertions):
    commands = []
    
    for ins in insertions:
        
        for i in range(len(string)):
        
            if string.startswith(ins.pair, i):
                commands.append( InsertOrder(i+1, ins.val) )

    commands.sort(reverse=True, key=return_InsertOrder_Pos)
    return commands
    
    
def part_1(poly_template, insertions, itterations=10):
    for i in range(itterations):
        print(i, end='')
        insert_commands = get_insert_commands(poly_template, insertions)    
        print('...', datetime.now())
        
        for command in insert_commands:
            poly_template = insert(poly_template, command.val, command.pos)
        
    poly_counter = Counter(poly_template)
    max_poly = poly_counter.most_common()[0][1]
    mix_poly = poly_counter.most_common()[-1][1]
    solution = max_poly - mix_poly
    return solution

    
def part_2(data):
    solution = None
    return solution    


def main():
    poly_template, insertions = load_data("..//Data//Prod.txt")
    poly_template_test, insertions_test = load_data("..//Data//Test.txt")
    
    # print( part_1(poly_template_test, insertions_test, 10) )
    print( part_1(poly_template, insertions, 40) )

    # assert part_1(data_test) == None
    # assert part_1(data) == None
    # assert part_2(data_test) == None
    # assert part_2(data) == None
    
    # [print(i) for i in insertions_test]
    # print(len(insertions_test))
   
    # print(part_1(poly_template_test, insertions_test))
    # print(part_2(data_test))
    # print(part_2(data))

if __name__ == "__main__":
    main()
