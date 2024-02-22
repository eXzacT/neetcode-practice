import numpy as np
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. '''


@time_execution(executions=1)  # Mutating the matrix so executions=1
def sol(matrix: list[list[int]]) -> None:
    matrix[:] = [list(reversed(row)) for row in zip(*matrix)]


@time_execution(executions=1)  # Mutating the matrix so executions=1
def sol_v2(matrix: list[list[int]]) -> None:
    WIDTH = HEIGHT = len(matrix)
    flatten = [el for row in matrix for el in row]
    matrix[:] = [flatten[-WIDTH+i::-WIDTH] for i in range(HEIGHT)]


@time_execution(executions=1)  # Mutating the matrix so executions=1
def sol_v3(matrix: list[list[int]]) -> None:
    WIDTH = len(matrix)  # Width and height are the same
    left, right = 0, WIDTH-1
    top, bottom = 0, WIDTH-1
    while left < right:
        for j in range(right-left):
            temp = matrix[top][left+j]
            matrix[top][left+j] = matrix[bottom-j][left]
            matrix[bottom-j][left] = matrix[bottom][right-j]
            matrix[bottom][right-j] = matrix[top+j][right]
            matrix[top+j][right] = temp

        left += 1
        right -= 1
        top += 1
        bottom -= 1


@time_execution(executions=1)  # Mutating the matrix so executions=1
def sol_v4(matrix: list[list[int]]) -> None:
    WIDTH = len(matrix)  # Width same as height in this problem

    def transpose(matrix: list[list[int]]) -> None:
        for i in range(WIDTH):
            for j in range(i+1, WIDTH):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reverse_rows(matrix: list[list[int]]) -> None:
        for row in range(WIDTH):
            left, right = 0, WIDTH-1
            while left < right:
                matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                left += 1
                right -= 1

    transpose(matrix)
    reverse_rows(matrix)


@time_execution(executions=1)  # Mutating the matrix so executions=1
def sol_np(matrix: list[list[int]]) -> None:
    matrix[:] = np.rot90(matrix, -1).tolist()
