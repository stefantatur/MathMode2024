import pathlib
import typing as tp
import random

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    spisok, groups, mass = [], [], []
    for i in values:
        groups.append(i)
        if len(groups) == n:
            spisok.append(groups)
            groups = mass.copy()
    return spisok


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    return grid[pos[0]]


def get_col(grid, pos):
    values = []
    for row in grid:
        values.append(row[pos[1]])
    return values


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    row, col = pos
    block = []
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(3):
            block.append(grid[i][start_col + j])
    return block


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if '.' == grid[row][col]:
                return row, col
    return -1, -1


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    proverka = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    values = set(list(set(get_block(grid, pos))) + list(set(get_col(grid, pos))) + list(set(get_row(grid, pos))))
    for i in range(10):
        if str(i) in values:
            proverka.remove(str(i))
    return set(proverka)


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    pos = find_empty_positions(grid)
    if pos == (-1, -1):
        return grid
    values = find_possible_values(grid, pos)
    for value in values:
        grid[pos[0]][pos[1]] = value
        if solve(grid):
            return grid
        grid[pos[0]][pos[1]] = '.'
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    for row in range(9):
        for col in range(9):
            pos = row, col
            if set(get_col(solution, pos)) == set(get_row(solution, pos)) and set(get_col(solution, pos)) == set(
                    get_block(solution, pos)):
                continue
            else:
                return False
    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    grid = [['.' for i in range(9)] for i in range(9)]
    puzzle = solve(grid)
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    if N > 81: return puzzle
    for pos in positions:
        flag = puzzle[pos[0]][pos[1]]
        puzzle[pos[0]][pos[1]] = '.'
        if not solve([row[:] for row in puzzle]):
            puzzle[pos[0]][pos[1]] = flag
        if sum(row.count('.') for row in puzzle) == 81 - N:
            return puzzle


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
