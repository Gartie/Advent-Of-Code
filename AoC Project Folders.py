import os

root = r"D:\Advent-Of-Code"
year = "2023"
month = "12"

py_file_content = """\'\'\' Day {{DAY}} of the {{YEAR}} Advent of Code
https://adventofcode.com/{{YEAR}}/day/{{DAY}}
https://adventofcode.com/{{YEAR}}/day/{{DAY}}/input \'\'\'

def load_data(Path):
    data_list = []
    with open(Path, 'r') as file:
        [data_list.append(line.strip()) for line in file]
    return data_list

    
def part_1(data):
    solution = None    
    return solution

    
def part_2(data):
    solution = None
    return solution    


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")
    
    # assert part_1(data_test) == None
    # assert part_1(data) == None
    # assert part_2(data_test) == None
    # assert part_2(data) == None
    
    print(part_1(data_test))
    # print(part_1(data))
    # print(part_2(data_test))
    # print(part_2(data))


if __name__ == "__main__":
    main()
"""

for n in range(1, 26):
    n1 = n
    n = str(n)
    if len(n) == 1:
        n = "0" + n

    project_path = f"{root}\\{year}\\Day {n}"

    if os.path.exists(project_path):
        continue

    data_path = f"{project_path}\\Data"
    src_path = f"{project_path}\\Src"
    py_file_path = f"{src_path}\\__main__.py"
    data_file_path = f"{data_path}\\Prod.txt"
    data_test_file_path = f"{data_path}\\Test.txt"
    todays_py_file_content = py_file_content.replace("{{YEAR}}", year)
    todays_py_file_content = todays_py_file_content.replace("{{DAY}}", str(n1))

    os.makedirs(project_path)
    os.makedirs(src_path)
    os.makedirs(data_path)
    with open(py_file_path, "w") as file:
        file.write(todays_py_file_content)
    with open(data_file_path, "w") as file:
        file.write("")
    with open(data_test_file_path, "w") as file:
        file.write("")
