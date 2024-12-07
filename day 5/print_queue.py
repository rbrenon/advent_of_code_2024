from pathlib import Path


def main():
    directory = Path.cwd()

    for filename in ['test', 'prod']:
        with Path.open(directory / "day 5" / filename) as file:
            data = file.read().splitlines()

        print(f"Part one ({filename}): {part_one(data)}")


def part_one(data: list[str]) -> int:
    # todo this cannot be a dict bc there are multiple vals per key and they overwrite previous maps
    instructions = dict()
    print_queue = list()

    for line in data:
        if '|' in line:
            before, after = map(int, (line.split('|')))
            if instructions.get(before):
                instructions[before].append(after)
            else: instructions[before] = [after]
        elif len(line) > 0:
            print_queue.append(list(map(int, (line.split(',')))))

    valid_print_jobs = list()
    for print_job in print_queue:
        valid_order = True
        printed_pages = set()
        for page in print_job:
            if sequences := instructions.get(page):
                if any(value in sequences for value in printed_pages):
                    valid_order = False
                    break
                else:
                    printed_pages.add(page)
            else:
                printed_pages.add(page)

        if valid_order:
            valid_print_jobs.append(print_job)

    sum_of_middle_pages = 0
    for valid_job in valid_print_jobs:
        sum_of_middle_pages += valid_job[len(valid_job) // 2]

    return sum_of_middle_pages  # 5690 - too high


if __name__ == "__main__":
    main()