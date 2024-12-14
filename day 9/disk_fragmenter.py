from pathlib import Path


def main():
    directory = Path.cwd()

    for filename in ["test", "prod"]:
        with Path.open(directory / "day 9" / filename) as file:
            data = file.read()

            print(f"Part 1 ({filename}): {part_one(data)}") # 90,033,860,628 - too low, 6,310,938,013,104 - too high


def part_one(data: str) -> int:
    block_map = create_block_map(data)
    # print(f"{block_map=} \n {len(block_map)=}")
    defragged_block_map = defrag_block_map(block_map)
    # print(f"{defragged_block_map=}")
    answer = calculate_checksum(defragged_block_map)
    # print(f"{answer=}")
    return answer


def calculate_checksum(defragged_block_map: list[tuple[int, int]]) -> int:
    return sum(
        a * b
        for a, b in defragged_block_map
    )


# todo 1; figure out how to use list vs string
def defrag_block_map(block_map: list) -> str:
    defragged_block_map = list()

    for i, block in enumerate(block_map):
        if "." in block:
            new_block = block_map.pop(-1)
            while "." in new_block:
                new_block = block_map.pop(-1)
            defragged_block_map.append((i, new_block[1]))
        else:
            defragged_block_map.append(block)

    return defragged_block_map


def create_block_map(data: str) -> list:
    block_map = list()
    block_no = 0

    for i, block in enumerate(data):
        if i % 2 == 0:
            # block will tell how many blocks for the file
            for b in range(int(block)):
                block_map.append((block_no, i // 2))
                block_no += 1
        else:
            # block will be how many open blocks until the next file
            for dot in range(int(block)):
                block_map.append((block_no, "."))
                block_no += 1
    return block_map


if __name__ == "__main__":
    main()
