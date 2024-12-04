import re

def main():
    for filename in ["test", "prod"]:
        with open(f"day 3/{filename}") as file:
            data = file.read()

        print(f"Part one ({filename}): {part_one(data)}")
        print(f"Part two ({filename}): {part_two(data)}")


def part_one(data: str) -> int:
    matches = re.findall("mul\([0-9]+,[0-9]+\)", data)

    sum_of_muls = 0
    for match in matches:
        _, a, b, _ = re.split('[(,)]', match)
        sum_of_muls += (int(a) * int(b))
    return sum_of_muls


def part_two(data:str) -> int:
    instructions = re.findall("mul\([0-9]+,[0-9]+\)|don\'t\(\)|do\(\)", data)
    sum_of_muls = 0

    calc = True

    for instruction in instructions:
        if "don't()" in instruction:
            calc = False
        elif 'do()' in instruction:
            calc = True

        if "mul" in instruction and calc == True:
            _, a, b, _ = re.split('[(,)]', instruction)
            sum_of_muls += (int(a) * int(b))
        
    return sum_of_muls


if __name__ == "__main__":
    main()