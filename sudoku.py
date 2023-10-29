from typing import List


def validate_sudoku_board(board: List[List[int]]) -> bool:
    """
    Validates a Sudoku board.

    Parameters:
    board (List[List[int]]): A 2D list representing a Sudoku board.

    Returns:
    bool: True if the board is valid, False otherwise.
    string: empty message if True, otherwise info about where the duplication happened
    """

    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num == '.':
                continue

            # Calculate the index of the 3x3 square this cell belongs to (29/10/2023)
            k = (i // 3) * 3 + j // 3

            if num in rows[i] or num in cols[j] or num in squares[k]:
                return False, f"Duplicate {num} found in row: {i+1}, column: {j+1})"

            rows[i].add(num)
            cols[j].add(num)
            squares[k].add(num)

    return True, ''
