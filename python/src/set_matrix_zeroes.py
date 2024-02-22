if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an m x n integer 'matrix', if an element is 0, set its entire row and column to 0's. You must do it in place.'''


@time_execution(executions=1)
def sol_naive(matrix: list[list[int]]) -> None:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)

    temp = [[el for el in row] for row in matrix]
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if matrix[i][j] == 0:
                for col in range(WIDTH):
                    temp[i][col] = 0
                for row in range(HEIGHT):
                    temp[row][j] = 0

    matrix[:] = temp


@time_execution(executions=1)
def sol(matrix: list[list[int]]) -> None:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    i_to_nullify = set()
    j_to_nullify = set()

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if matrix[i][j] == 0:
                i_to_nullify.add(i)
                j_to_nullify.add(j)

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if i in i_to_nullify or j in j_to_nullify:
                matrix[i][j] = 0


@time_execution(executions=1)
def sol_v2(matrix: list[list[int]]) -> None:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    rows = [False]*HEIGHT
    cols = [False]*WIDTH

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if matrix[i][j] == 0:
                rows[i] = True
                cols[j] = True

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if rows[i] or cols[j]:
                matrix[i][j] = 0


@time_execution(executions=1)
def sol_v3(matrix: list[list[int]]) -> None:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    first_col = False  # Should we set first column to zero?

    # Mark elements in first row/col, this tells us later which row and column should be zeroed out
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                if j == 0:  # First column should also be zeroed out
                    first_col = True
                else:
                    matrix[0][j] = 0

    # Change all the elements whose row and column was marked, but don't touch first row and first column for now
    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Change the entire first row to 0
    if matrix[0][0] == 0:
        for j in range(WIDTH):
            matrix[0][j] = 0

    # Also change the column
    if first_col:
        for i in range(HEIGHT):
            matrix[i][0] = 0
