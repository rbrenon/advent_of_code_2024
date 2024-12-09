from pathlib import Path
from itertools import product
import re


def main():
    directory = Path.cwd()

    for filename in ['test', 'prod']:
        with Path.open(directory / "day 7" / filename) as file:
            data = file.read().splitlines()

            print(f"Part one ({filename}): {part_one(data)}")   # 5512534574980


def part_one(data:list[str]) -> int:
    valid_equations = list()
    
    for line in data:
        answer, values = line.split(":")
        answer = int(answer)
        values = [int(val) for val in values.strip().split()]

        if valid := find_valid_combo(answer=answer, values=values):
            valid_equations.append(valid)

    return sum(valid_equations)


def find_valid_combo(answer: int, values: list[int]):
    number_of_operators = len(values) - 1
    operators_to_try = list(product("*+", repeat=number_of_operators))

    for operators in operators_to_try:
        equation = str()
        for i, value in enumerate(values):
            equation += str(value)
            equation = eval(equation)
            try:
                equation = str(equation) + operators[i]
            except IndexError as ie:
                if equation == answer:
                    return answer


if __name__ == "__main__":
    main()