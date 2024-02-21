if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an m x n matrix, return all elements of the matrix in res order.'''


@time_execution()
def sol_complex(matrix: list[list[int]]) -> list[int]:
    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    res = []
    seen = set()

    def helper(pos: complex, d: complex) -> None:
        # Any time we reach the edge or a seen position
        if not (0 <= pos.real < HEIGHT and 0 <= pos.imag < WIDTH) or pos in seen:
            nd = d*-1j
            # Go back by 1 step then go 1 step in the 90 degrees clockwise from the current direction
            newpos = pos-d+nd
            # We've reached the end of the spiral since even by rotating 90 degrees we still hit a "wall"
            if newpos in seen or not (0 <= newpos.real < HEIGHT and 0 <= newpos.imag < WIDTH):
                return
            helper(newpos, d*-1j)
        else:  # Otherwise keep going in the same direction
            seen.add(pos)
            res.append(matrix[int(pos.real)][int(pos.imag)])
            helper(pos+d, d)

    helper(0+0j, 1j)  # Start from top left and go right
    return res


@time_execution()
def sol(matrix: list[list[int]]) -> list[int]:
    def rotate_90_clockwise(d: tuple[int, int]):
        x, y = d
        return y, -x

    WIDTH = len(matrix[0])
    HEIGHT = len(matrix)
    seen = set()
    res = []
    x, y, d = 0, 0, (0, 1)  # Start from top left and go right

    while True:
        if x < 0 or x >= HEIGHT or y < 0 or y >= WIDTH or (x, y) in seen:
            x, y = x-d[0], y-d[1]  # Step backwards using direction
            d = rotate_90_clockwise(d)
            x, y = x+d[0], y+d[1]  # Step forwards using new direction
            # We've reached the end of the spiral since even by rotating 90 degrees we still hit a "wall"
            if (x, y) in seen or x < 0 or x >= HEIGHT or y < 0 or y >= WIDTH:
                return res

        res.append(matrix[x][y])
        seen.add((x, y))
        x, y = x+d[0], y+d[1]


@time_execution()
def sol_space_optimized(matrix: list[list[int]]) -> list[int]:
    def rotate_90_clockwise(d: tuple[int, int]):
        x, y = d
        return y, -x

    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    res = []
    x, y, d = 0, 0, (0, 1)  # Start from top left and go right

    while True:
        res.append(matrix[x][y])
        x, y = x+d[0], y+d[1]
        if y < left or y >= right or x < top or x >= bottom:  # Hit a boundary
            match d:  # Shrink boundaries accordingly
                case 0, 1:
                    top += 1
                case 1, 0:
                    right -= 1
                case 0, -1:
                    bottom -= 1
                case -1, 0:
                    left += 1

            x, y = x-d[0], y-d[1]  # Step backwards using direction
            d = rotate_90_clockwise(d)
            x, y = x+d[0], y+d[1]  # Step forwards using new direction
            if y < left or y >= right or x < top or x >= bottom:
                return res


@time_execution()
def sol_space_optimized_v2(matrix: list[list[int]]) -> list[int]:
    left, right = 0, len(matrix[0])
    top, bottom = 0, len(matrix)
    res = []

    while left < right and top < bottom:
        for i in range(left, right):
            res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1

        if not (left < right and top < bottom):  # Edge cases for single row/single col matrices
            break

        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom-1][i])
        bottom -= 1

        for i in range(bottom-1, top-1, -1):
            res.append(matrix[i][left])
        left += 1

    return res
