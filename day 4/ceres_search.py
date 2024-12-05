from pathlib import Path
import re
import numpy as np


def main():
    directory = Path.cwd()
    for filename in ['test']:
        with Path.open(directory / "day 4" / filename) as file:
            data = file.read().splitlines()

            print(f"Part one ({filename}): {part_one(data)}")


def part_one(data: list[str]) -> int:
    parsed_data = [list(strings) for strings in data]

    matrix = np.array(parsed_data)
    sum_of_xmas = 0

    # find horizontal 
    sum_of_xmas += find_xmas(matrix)

    # find vertical
    transposed_matrix = np.transpose(matrix)
    sum_of_xmas += find_xmas(transposed_matrix)

    # find diagonals
    diagonal_matrix = np.diag(matrix, k=-1)
    sum_of_xmas += find_xmas(diagonal_matrix)
    # flipped_diag_matrix = np.fliplr(diagonal_matrix).diagonal()
    # sum_of_xmas += find_xmas(flipped_diag_matrix)

    return sum_of_xmas


def find_xmas(data: list[str]) -> int:
    found = 0

    for line in data:
        joined_line = ''.join(line)
        found += len(re.findall("XMAS", joined_line))
        found += len(re.findall("SAMX", joined_line))

    return found
    




if __name__ == "__main__":
    main()