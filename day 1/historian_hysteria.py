from pathlib import Path
from collections import Counter


def main():
    directory = Path.cwd()
    for filename in ['test', 'prod']:
        with Path.open(directory / "day 1" / filename) as file:
            data = file.read().splitlines()

            print(f"Part 1 ({filename}): {part_one(data)}")
            print(f"Part 2 ({filename}): {part_two(data)}")


def part_one(data: list[str]) -> int:
    col_a, col_b = list(), list()

    for line in data:
        col_a.append(eval(line.split()[0]))
        col_b.append(eval(line.split()[1]))

    col_a.sort()
    col_b.sort()

    sorted_lists = (tuple(zip(col_a, col_b)))

    delta_of_reconcilled_lists = [abs(a-b) for a, b in sorted_lists]

    return sum(delta_of_reconcilled_lists)


def part_two(data: list[str]) -> int:
    col_a, col_b = list(), list()

    for line in data:
        col_a.append(eval(line.split()[0]))
        col_b.append(eval(line.split()[1]))

    sum_of_col_a_values_in_col_b = 0

    col_b_counter = Counter(col_b)

    for element in col_a:
        sum_of_col_a_values_in_col_b += (element * col_b_counter[element])

    return sum_of_col_a_values_in_col_b   


if __name__ == "__main__":
    main()