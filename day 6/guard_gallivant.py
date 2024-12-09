from pathlib import Path


def main():
    directory = Path.cwd()

    for filename in ['test']:
        with Path.open(directory/"day 6/test") as file:
            data = file.read().splitlines()

            print(f"Part one {filename}: {part_one(data)}")


def part_one(data: list[str]) -> int:
    starting_point = find_starting_point(data)
    starting_row, starting_col = starting_point
    steps_taken = 0
    step_direction:bool = True

    while starting_point:
        data = transpose_matrix(data) 
        starting_row, starting_col = starting_col, starting_row
        step_direction = not(step_direction)
        # look for next hash in the same row as the starting point passing only that row
        steps_to_next_hash, starting_row = find_next_hash(data[starting_row], starting_col, direction=step_direction) # count down
        if steps_to_next_hash:
            steps_taken += steps_to_next_hash
        else: 
            return steps_taken
        print(f"{steps_to_next_hash=}, {steps_taken=}, {starting_col=}")
    

    return


def find_next_hash(data: list[str], col: int, direction:bool) -> tuple[int, tuple[int,int]]: 
    steps_to_reach_next_hash = 0
    
    # search row from current row coord down to zero to find the next #   
    if direction:
        step_dir = 1
        stop = len(data)
    else: 
        step_dir = -1
        stop = -1

    ri = col
    for row in range(col, stop, step_dir):
    # for ri, row in enumerate(data, start=col, step=step_dir):
        if data[row] == ".":
            steps_to_reach_next_hash += 1
            ri += step_dir
        elif data[row] == '#':
            new_starting_point = ri
            steps_to_reach_next_hash += 1
            return (steps_to_reach_next_hash, new_starting_point)

    return None, None


def transpose_matrix(data: list[str]) -> list[str]:
    transposed_matrix = list()

    for ir, row in enumerate(data):
        new_row = list()
        for ic, col in enumerate(row):
            new_row.extend(data[ic][ir])
        transposed_matrix.append(''.join(new_row))
        
    print(*transposed_matrix, sep="\n")
    return transposed_matrix


def find_starting_point(data:list[str]) -> tuple[int,int]:
    for ir, row in enumerate(data):
        for ic, col in enumerate(row):
            if data[ir][ic] == "^":
                return (ir, ic)
            
        

def numb_steps_to_hash(line: list[str]) -> int:
    ...




if __name__ == "__main__":
    main()