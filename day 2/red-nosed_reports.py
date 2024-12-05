from pathlib import Path
from collections import Counter


def main():
    directory = Path.cwd()
    for filename in ["test", "prod"]:  #
        with Path.open(directory / "day 2" / filename) as file:
            data = file.read().strip().splitlines()

            print(f"Part one ({filename}): {part_one(data)}")
            print(f"Part two ({filename}): {part_two(data)}")


def part_one(reports: list[str]) -> int:
    valid_reports = 0

    for report in reports:
        report_result = set()
        numbs = [int(x) for x in report.split()]
        for n_i, numb in enumerate(numbs):
            if n_i + 1 < len(numbs):
                if numbs[n_i + 1] > numb and abs(numbs[n_i + 1] - numb) <= 3:
                    report_result.add("lt")
                elif numbs[n_i + 1] < numb and abs(numbs[n_i + 1] - numb) <= 3:
                    report_result.add("gt")
                else:
                    report_result.add("ng")
        if len(report_result) == 1 and "ng" not in report_result:
            valid_reports += 1

    return valid_reports


def part_two(reports: list[str]) -> int:
    valid_reports = 0

    for report in reports:
        report_result = list()
        
        numbs = [int(x) for x in report.split()]
        for n_i, numb in enumerate(numbs):
            if n_i + 1 < len(numbs):
                report_result.append(numbs[n_i + 1] - numb)

        count = Counter(report_result)

        if (max(count) <= 3 and min(count) >= -3) and (
            (
                all([x[0] < 0 for x in count.items()])
                or [x[0] >= 0 for x in count.items()].count(True) == 1
                )
            
            or (
                all([x[0] > 0 for x in count.items()])
                or [x[0] <= 0 for x in count.items()].count(True) == 1
                )
        ):
            valid_reports += 1

    return valid_reports  # 484 - too high; 354 - too low; 361, 390 - unk


if __name__ == "__main__":
    main()
