''' Day 15 of the 2023 Advent of Code
https://adventofcode.com/2023/day/15
https://adventofcode.com/2023/day/15/input '''

def load_data(Path):
    data_list = []
    with open(Path, 'r') as file:
        file = file.read()
        file = file.strip()
        data_list = file.split(",")
    return data_list

def HASH_operation(curr, char):
    ascii_value = ord(char)
    curr += ascii_value
    curr *= 17
    curr %= 256
    return curr

 
def HASHMAP_operation(word):
    HASH_value = -1
    operation = ""
    focal_length = -1
    label = ""

    for char in word:
        if char in "-=":
            operation = char
            continue
        if char.isdigit():
            focal_length = int(char)
            continue
        
        label += char
        HASH_value = max(0, HASH_value)
        HASH_value = HASH_operation(HASH_value, char)

    if HASH_value == -1 or not operation or not label or (operation == "=" and focal_length == -1):
        raise RuntimeError(f"Error on: {word} {label} {operation} {focal_length} {HASH_value}")

    return (label, HASH_value, operation, focal_length)


def part_1(data):
    solution = 0
    for word in data:
        curr_value = 0
        
        for char in word:
            curr_value = HASH_operation(curr_value, char)
        
        solution += curr_value
    
    return solution

    
def part_2(data):
    solution = 0
    boxes = [ {} for _ in range(256) ]
 
    for word in data:
        label, HASH_value, operation, focal_length = HASHMAP_operation(word)
        if operation == "-":
            boxes[HASH_value].pop(label, None)
            continue
            
        if operation == "=":
            boxes[HASH_value][label] = focal_length
            continue
    
    for box_index, box in enumerate(boxes):
        for item_index, focal_length in enumerate(box.values()):
            solution += (box_index+1)*(item_index+1)*focal_length
        
    return solution    


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    
    assert part_1(data_test) == 1320
    assert part_1(data) == 505459
    assert part_2(data_test) == 145
    assert part_2(data) == 228508


if __name__ == "__main__":
    main()
