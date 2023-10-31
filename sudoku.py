def validate_sudoku_board(board: list[list[int]]) -> tuple[bool, str]:
    """
    Validates a Sudoku board.

    Parameters:
    board (List[List[int]]): A 2D list representing a Sudoku board.

    Returns:
    Tuple[bool, str]: A tuple where the first element is a boolean indicating 
                      whether the board is valid (True) or not (False), and 
                      the second element is a string that is empty if the board 
                      is valid, or contains information about where the duplication 
                      occurred if the board is invalid.
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
