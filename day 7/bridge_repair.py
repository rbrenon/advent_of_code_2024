from pathlib import Path
from itertools import product


def main():
    directory = Path.cwd()

    for filename in ['test']:
        with Path.open(directory / "day 7" / filename) as file:
            data = file.read().splitlines()

            print(f"Part one ({filename}): {part_one(data)}")


def part_one(data:list[str]) -> int:
    valid_equations = list()
    
    for line in data:
        answer, values = line.split(":")
        answer = int(answer)
        values = [int(val) for val in values.strip().split()]

        if find_valid_combo(answer=answer, values=values):
            valid_equations.extend(values)

        print(f"{answer=} {values=}")

    return sum(valid_equations)


def find_valid_combo(answer: int, values: list[int]):
    number_of_operators = len(values) - 1

    operators_to_try = list(product("*+", repeat=number_of_operators))

    for operator in operators_to_try:
        # interleaved_list = list(*zip(values), operators_to_try)

        print(f"{operator=} - {operators_to_try=}")

    


if __name__ == "__main__":
    main()