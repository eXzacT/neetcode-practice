from collections import defaultdict

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Determine if a 9 x 9 Sudoku board is valid.
    Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.'''


@time_execution(executions=100)
def sol(board: list[list[int]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue

            # Calculate the index of the 3x3 square this cell belongs to
            k = (i // 3) * 3 + j // 3

            if num in rows[i] or num in cols[j] or num in squares[k]:
                return False

            rows[i].add(num)
            cols[j].add(num)
            squares[k].add(num)

    return True


@time_execution(executions=100)
def sol_v2(board: list[list[int]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    squares = defaultdict(set)

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue

            # Calculate the index of the 3x3 square this cell belongs to
            k = (i // 3) * 3 + j // 3

            if num in rows[i] or num in cols[j] or num in squares[k]:
                return False

            rows[i].add(num)
            cols[j].add(num)
            squares[k].add(num)

    return True
