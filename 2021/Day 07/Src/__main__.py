""" Day 07 of the 2021 Advent of Code
https://adventofcode.com/2021/day/7
https://adventofcode.com/2021/day/7/input """


def load_data(path):
    data_list = []
    with open(path, "r") as file:
        for line in file:
            data_list = data_list + [int(value.strip()) for value in line.split(",")]
    return data_list


def calculate_crab_fuel_needs(data, fuelcomsumption_increases=False):
    solution = -1

    for target in range(max(data)):
        local_score = 0

        for start in data:
            steps = abs(target - start)

            if not fuelcomsumption_increases:
                # part 1
                local_score = local_score + steps
            else:
                # part 2
                local_score = local_score + sum(list(range(steps + 1)))

            # early skip if local score is escalating the pan out
            # saves 35s on excecutiontime when solving part 2
            if local_score > solution and solution != -1:
                break

        if local_score < solution or solution == -1:
            solution = local_score

    return solution


def main():
    data = load_data("..//Data//Prod.txt")
    data_test = load_data("..//Data//Test.txt")

    assert calculate_crab_fuel_needs(data_test, False) == 37
    assert calculate_crab_fuel_needs(data, False) == 357353
    assert calculate_crab_fuel_needs(data_test, True) == 168
    assert calculate_crab_fuel_needs(data, True) == 104822130


if __name__ == "__main__":
    main()
