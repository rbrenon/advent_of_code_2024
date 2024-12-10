from pathlib import Path
from itertools import product
import re


def main():
    directory = Path.cwd()

    for filename in ["test", "prod"]:
        with Path.open(directory / "day 7" / filename) as file:
            data = file.read().splitlines()

            p1 = part_one(data)
            p2 = part_two(
                data, p1
            )  # adding list of valid equations (answer only) that can be dropped from computation
            print(f"Part one ({filename}): {sum(p1)}")  # 5512534574980
            print(f"Part two ({filename}): {sum(p2)}")  # 328790210468594


def part_one(data: list[str]) -> list[int]:
    valid_equations = list()

    for line in data:
        answer, values = line.split(":")
        answer = int(answer)
        values = [int(val) for val in values.strip().split()]

        if valid := find_valid_combo(answer=answer, values=values):
            valid_equations.append(valid)

    return valid_equations


def part_two(data: list[str], already_validated: list[int]) -> list[int]:
    valid_equations = list()

    for line in data:
        answer, values = line.split(":")
        answer = int(answer)

        if answer in already_validated:
            valid_equations.append(answer)
        else:
            values = [int(val) for val in values.strip().split()]

            if valid := find_valid_combo_with_join(answer=answer, values=values):
                valid_equations.append(valid)

    return valid_equations


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


def find_valid_combo_with_join(answer, values):
    number_of_operators = len(values) - 1
    operators_to_try = list(product("*+|", repeat=number_of_operators))

    for operators in operators_to_try:
        if "|" in operators:
            equation = str()
            for i, value in enumerate(values):
                equation += str(value)
                if "|" in equation:
                    equation = "".join(equation.split("|"))
                equation = eval(equation)
                try:
                    equation = str(equation) + operators[i]
                except IndexError as ie:
                    if equation == answer:
                        return answer


if __name__ == "__main__":
    main()
