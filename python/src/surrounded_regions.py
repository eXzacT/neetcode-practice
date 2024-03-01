if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.
    A region is captured by flipping all 'O's into 'X's in that surrounded region.'''


@time_execution(executions=1)  # Mutating original board
def sol_dfs(board: list[list[str]]) -> None:
    WIDTH = len(board[0])
    HEIGHT = len(board)

    def visit_peninsulas(i: int, j: int) -> None:
        # Mark as visited and go in all 4 directions if it's still an island and in bounds
        visited[i][j] = True
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and board[ni][nj] == 'O' and not visited[ni][nj]:
                visit_peninsulas(ni, nj)

    visited = [[False]*WIDTH for _ in range(HEIGHT)]

    # Start visiting the remainder of the peninsula from every edge position on the board
    for j in range(WIDTH):
        if board[0][j] == 'O' and not visited[0][j]:
            visit_peninsulas(0, j)
        if board[HEIGHT-1][j] == 'O' and not visited[HEIGHT-1][j]:
            visit_peninsulas(HEIGHT-1, j)
    for i in range(HEIGHT):
        if board[i][0] == 'O' and not visited[i][0]:
            visit_peninsulas(i, 0)
        if board[i][WIDTH-1] == 'O' and not visited[i][WIDTH-1]:
            visit_peninsulas(i, WIDTH-1)

    for i in range(HEIGHT):
        for j in range(WIDTH):
            # We couldn't reach this position, so it means it's fully surrounded by water, capture it
            if not visited[i][j]:
                board[i][j] = 'X'


@time_execution(executions=1)  # Mutating original board
def sol_dfs_iter(board: list[list[str]]) -> None:
    WIDTH = len(board[0])
    HEIGHT = len(board)

    def visit_peninsulas(i: int, j: int) -> None:
        stack = [(i, j)]
        while stack:
            i, j = stack.pop()
            if 0 <= i < HEIGHT and 0 <= j < WIDTH and board[i][j] == 'O':
                board[i][j] = 'E'  # Mark as visited by changing 'O' to 'E'
                stack.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

    # Start visiting the remainder of the peninsula from every edge position on the board
    for j in range(WIDTH):
        if board[0][j] == 'O':
            visit_peninsulas(0, j)
        if board[HEIGHT-1][j] == 'O':
            visit_peninsulas(HEIGHT-1, j)
    for i in range(HEIGHT):
        if board[i][0] == 'O':
            visit_peninsulas(i, 0)
        if board[i][WIDTH-1] == 'O':
            visit_peninsulas(i, WIDTH-1)

    # Capture all 'O's since we couldn't reach them from any edge position, they are surrounded
    # Change all 'E's back to 'O's because they can't be captured
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                board[i][j] = 'O'


@time_execution(executions=1)  # Mutating original board
def sol_dfs_iter_v2(board: list[list[str]]) -> None:
    WIDTH = len(board[0])
    HEIGHT = len(board)

    def visit_peninsulas(i: int, j: int) -> None:
        stack = [(i, j)]
        board[i][j] = 'E'

        while stack:
            i, j = stack.pop()
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and board[ni][nj] == 'O':
                    board[ni][nj] = 'E'
                    stack.append((ni, nj))

    # Start visiting the remainder of the peninsula from every edge position on the board
    for j in range(WIDTH):
        if board[0][j] == 'O':
            visit_peninsulas(0, j)
        if board[HEIGHT-1][j] == 'O':
            visit_peninsulas(HEIGHT-1, j)
    for i in range(HEIGHT):
        if board[i][0] == 'O':
            visit_peninsulas(i, 0)
        if board[i][WIDTH-1] == 'O':
            visit_peninsulas(i, WIDTH-1)

    # Capture all 'O's since we couldn't reach them from any edge position, they are surrounded
    # Change all 'E's back to 'O's because they can't be captured
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                board[i][j] = 'O'
