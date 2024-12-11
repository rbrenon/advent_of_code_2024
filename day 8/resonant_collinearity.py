from pathlib import Path
from itertools import combinations


def main():
    directory = Path.cwd()

    for filename in ["test", "prod"]:
        with Path.open(directory / "day 8" / filename) as file:
            data = file.read().splitlines()

        print(f"Part one ({filename}): {part_one(data)}")  # 380 too high, 367
        print(f"Part two ({filename}): {part_two(data)}")


def part_one(data: list[str]) -> int:
    antennas = find_antennas(data)

    max_col = len(data[0])
    max_row = len(data)
    antinodes = find_antinodes(antennas, max_row, max_col)

    return antinodes


def find_antinodes(
    antennas: dict[list[tuple[int, int]]], max_row: int, max_col: int
) -> int:
    antinodes = list()

    for antenna in antennas:
        antenna_combinations = list(combinations(antennas[antenna], r=2))
        antinodes.extend(calculate_antinodes(antenna_combinations, max_row, max_col))

    # print(set(antinodes))
    return len(set(antinodes))


def calculate_antinodes(
    antenna_combinations: list[tuple[tuple[int, int], tuple[int, int]]],
    max_row: int,
    max_col: int,
) -> list:
    new_antinodes = list()

    for antenna_pair in antenna_combinations:
        row_delta = antenna_pair[0][0] - antenna_pair[1][0]
        col_delta = antenna_pair[0][1] - antenna_pair[1][1]

        for antenna_point in antenna_pair:
            negative_antinode = (
                antenna_point[0] - row_delta,
                antenna_point[1] - col_delta,
            )
            positive_antinode = (
                antenna_point[0] + row_delta,
                antenna_point[1] + col_delta,
            )
            if (
                negative_antinode not in antenna_pair
                and 0 <= negative_antinode[0] < max_row
                and 0 <= negative_antinode[1] < max_col
            ):
                new_antinodes.append(negative_antinode)
            if (
                positive_antinode not in antenna_pair
                and 0 <= positive_antinode[0] < max_row
                and 0 <= positive_antinode[1] < max_col
            ):
                new_antinodes.append(positive_antinode)

    return new_antinodes


def find_antennas(data: list[str]) -> dict[list[tuple[int, int]]]:
    antennas = dict()

    for ri, row in enumerate(data):
        for ci, col in enumerate(row):
            if col != ".":
                if antennas.get(col):
                    antennas[col].append((ri, ci))
                else:
                    antennas[col] = [(ri, ci)]

    return antennas


def part_two(data: list[str]) -> int: ...


if __name__ == "__main__":
    main()
