if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given a positive integer n, how many ways can we put n queens on a chess board of size n*n in such way that the queens don't attack each other
    Return all distinct solutions to the n-queens puzzle. You may return the answer in any order.'''


@time_execution()
def sol_naive(n: int) -> list[list[str]]:
    def can_place(row: int, col: int) -> bool:
        for i in range(row):
            if board[i][col]:  # Check above
                return False
            l_diagonal_col = col-row+i
            # Check left diagonal
            if 0 <= l_diagonal_col < n and board[i][l_diagonal_col]:
                return False
            r_diagonal_col = col+row-i
            # Check right diagonal
            if 0 <= r_diagonal_col < n and board[i][r_diagonal_col]:
                return False

        return True

    def place(row: int, combination: str = "") -> None:
        if row == n:  # Managed to place n queens if we got to the last row
            # Partition the string into n rows
            combinations.append([combination[i:i+n] for i in range(0, n*n, n)])
            return

        for col in range(n):
            if can_place(row, col):
                board[row][col] = True
                place(row+1, combination+"."*(col)+"Q"+"."*(n-col-1))
                board[row][col] = False

    board = [[False]*n for _ in range(n)]
    combinations = []
    place(0)
    return combinations


@time_execution()
def sol_naive_complex(n: int) -> int:
    def can_place(pos: complex) -> bool:
        for i in range(int(pos.real)):
            if board[complex(i, pos.imag)]:  # Check above
                return False
            # Returning 0 by default if we go out of bounds, which won't take that position into consideration, still might return True
            if board.get(complex(i, pos.imag - (pos.real - i)), 0):  # Left diagonal
                return False
            if board.get(complex(i, pos.imag + (pos.real - i)), 0):  # Right diagonal
                return False
        return True

    def place(row: int) -> None:
        if row == n:  # Managed to place n queens if we got to the last row
            # Partition the string into n rows
            combinations.append(
                [''.join(["Q" if board[complex(i, j)] else "." for j in range(n)])for i in range(n)])
            return

        # Check if we can place the queen anywhere on this row
        for new_pos in [complex(row, col) for col in range(n)]:
            if can_place(new_pos):
                board[new_pos] = 1  # Place the queen
                place(row+1)
                board[new_pos] = 0  # Remove the queen for backtracking

    combinations = []
    board = {complex(i, j): 0 for i in range(n)
             for j in range(n)}

    place(0)
    return combinations


@time_execution()
def sol_optimized(n: int) -> list[list[str]]:
    def place(row: int, combination: str = "") -> None:
        if row == n:  # Managed to place n queens if we got to the last row
            # Partition the string into n rows
            combinations.append([combination[i:i+n] for i in range(0, n*n, n)])
            return

        for col in range(n):
            minor_idx = row+col
            major_idx = n-1-(row-col)

            if not cols[col] and not major_diagonals[major_idx] and not minor_diagonals[minor_idx]:
                # Place
                cols[col] = True
                minor_diagonals[minor_idx] = True
                major_diagonals[major_idx] = True

                place(row+1, combination+"."*(col)+"Q"+"."*(n-col-1))

                # Remove
                cols[col] = False
                minor_diagonals[minor_idx] = False
                major_diagonals[major_idx] = False

    cols = [False]*n
    major_diagonals = [False]*(2*n-1)
    minor_diagonals = [False]*(2*n-1)

    combinations = []
    place(0)
    return combinations
