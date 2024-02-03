import numpy as np

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.
    Return true if a given target is in matrix or false otherwise.'''


@time_execution()
def sol_naive(matrix: list[list[int]], needle: int) -> int:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if matrix[i][j] == needle:
                return True

    return False


@time_execution()
def sol_naive_np(matrix: list[list[int]], needle: int) -> int:
    return needle in np.array(matrix)


@time_execution()
def sol_mlogn(matrix: list[list[int]], needle: int) -> int:
    for row in matrix:
        lo = 0
        hi = len(row)-1
        while lo <= hi:
            mid = lo+(hi-lo)//2
            if row[mid] == needle:
                return True
            if needle < row[mid]:
                hi = mid-1
            else:
                lo = mid+1

    return False


@time_execution()
def sol_logmlogn(matrix: list[list[int]], needle: int) -> int:
    WIDTH, HEIGHT = len(matrix[0]), len(matrix)
    lo, hi = 0, HEIGHT-1

    while lo <= hi:
        row = lo+(hi-lo)//2
        if matrix[row][0] == needle:
            return True
        if needle < matrix[row][0]:
            hi = row-1
        elif needle > matrix[row][-1]:
            lo = row+1
        else:  # Found possible row
            break
    else:  # Else happens if break doesn't happen, so value is for sure not in any rows
        return False

    # Same as else: because lo will be bigger than hi only if we didn't break from prev loop
    # if lo > hi:
    #     return False

    # Now check the row
    col_lo, col_hi = 0, WIDTH-1
    while col_lo <= col_hi:
        mid = col_lo+(col_hi-col_lo)//2
        if matrix[row][mid] == needle:
            return True
        if needle < matrix[row][mid]:
            col_hi = mid-1
        else:
            col_lo = mid+1

    return False
