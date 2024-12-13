from pathlib import Path


def main():
    directory = Path.cwd()

    for filename in ["test"]:#, "prod"]:
        with Path.open(directory / "day 9" / filename) as file:
            data = file.read()

            print(f"Part 1 ({filename}): {part_one(data)}") # 90033860628 - too low


def part_one(data: str) -> int:
    block_map = create_block_map(data)
    print(f"{block_map=}")
    defragged_block_map = defrag_block_map(block_map)
    print(f"{defragged_block_map=}")
    answer = calculate_checksum(defragged_block_map)
    print(f"{answer=}")
    return answer


def calculate_checksum(defragged_block_map: str) -> int:
    return sum(
        a * b
        for a, b in zip(
            [int(x) for x in defragged_block_map], list(range(len(defragged_block_map)))
        )
    )


def defrag_block_map(block_map: str) -> str:
    defragged_block_map = str()
    block_map = [ch for ch in block_map]

    for i, block in enumerate(block_map):
        while block == ".":
            block_map[i] = block_map.pop(-1)
            block = block_map[i]

        defragged_block_map += block

    return defragged_block_map


def create_block_map(data: str) -> str:
    block_map = str()

    for i, block in enumerate(data):
        if i % 2 == 0:
            block_map += str(i // 2) * int(block)
        else:
            block_map += "." * int(block)

    return block_map


if __name__ == "__main__":
    main()
