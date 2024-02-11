from collections import Counter
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


''' Given an m x n grid of characters board and a string target, return true if target exists in the grid.
    The target can be constructed from letters of sequentially adjacent cells, it is allowed to go vertically or horizontally
    The same letter cell may not be used more than once.'''


@time_execution()
def sol_iter(board: list[list[str]], target: str) -> bool:
    HEIGHT = len(board)
    WIDTH = len(board[0])

    # All the positions on the board that have the correct starting char
    stack = [((i, j), 0, set()) for i in range(HEIGHT)
             for j in range(WIDTH) if board[i][j] == target[0]]

    while stack:
        (x, y), idx, seen = stack.pop()
        seen = seen.copy()

        if idx == len(target):  # Full match
            return True

        # Inside bounds, didn't see before and character at current position is same as the one we're looking for
        if 0 <= x < HEIGHT and 0 <= y < WIDTH and (x, y) not in seen and board[x][y] == target[idx]:
            seen.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                stack.append(((x+dx, y+dy), idx+1, seen))

    return False


@time_execution()
def sol_iter_v2(board: list[list[str]], target: str) -> bool:
    HEIGHT = len(board)
    WIDTH = len(board[0])

    # All the positions on the board that have the correct starting char
    stack = [((i, j), 0, [[False]*WIDTH for _ in range(HEIGHT)]) for i in range(HEIGHT)
             for j in range(WIDTH) if board[i][j] == target[0]]

    while stack:
        (x, y), idx, seen = stack.pop()

        if idx == len(target)-1:
            return True

        seen = [row[:] for row in seen]
        seen[x][y] = True

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x+dx, y+dy
            # In bounds, didn't see before and matches the next character
            if 0 <= nx < HEIGHT and 0 <= ny < WIDTH and not seen[nx][ny] and board[nx][ny] == target[idx+1]:
                stack.append(((nx, ny), idx+1, seen))

    return False


@time_execution()
def sol_iter_complex(board: list[list[str]], target: str) -> bool:
    board: dict[complex, str] = {complex(i, j): char for i, row in enumerate(board)
                                 for j, char in enumerate(row)}

    stack = [(pos, 1, set([pos]))
             for pos, char in board.items() if char == target[0]]
    while stack:
        pos, idx, seen = stack.pop()
        if idx == len(target):
            return True

        seen = seen.copy()
        seen.add(pos)
        for new_pos in [pos+1, pos-1, pos-1j, pos+1j]:
            if new_pos in board and new_pos not in seen:  # Inside bounds and haven't seen before
                if board[new_pos] == target[idx]:
                    stack.append((new_pos, idx+1, seen))

    return False  # No match found after checking all cells


@time_execution()
def sol_rec(board: list[list[str]], target: str) -> bool:
    def helper(i: int, j: int, idx: int, seen: set) -> bool:
        # Out of bounds, found a character that doesn't match or already used this char
        if i == -1 or i == HEIGHT or j == -1 or j == WIDTH or board[i][j] != target[idx] or (i, j) in seen:
            return False

        seen = seen.copy()
        seen.add((i, j))
        # Character matches, check in all 4 directions or return True if we reached end of target
        if board[i][j] == target[idx]:
            if idx == len(target)-1:
                return True

            return helper(i-1, j, idx+1, seen) or helper(i+1, j, idx+1, seen) or helper(i, j-1, idx+1, seen) or helper(i, j+1, idx+1, seen)

        if j+1 == WIDTH:  # Can't go right, change rows and reset j to 0
            return helper(i+1, 0, idx, seen)
        else:  # Go right
            return helper(i, j+1, idx, seen)

    HEIGHT = len(board)
    WIDTH = len(board[0])
    # For every first character of a wanted target, check recursively whether we can make the rest of the target
    return any(helper(i, j, 0, set()) for i in range(HEIGHT)
               for j in range(WIDTH) if board[i][j] == target[0])


@time_execution()
def sol_rec_v2(board: list[list[str]], target: str) -> bool:
    def helper(i: int, j: int, idx: int) -> bool:
        if idx == len(target):
            return True
        # Out of bounds, found a character that doesn't match or already used this char
        if i == -1 or i == HEIGHT or j == -1 or j == WIDTH or board[i][j] != target[idx] or (i, j) in seen:
            return False

        # Go in all directions, and remove from seen if this path ended up being false
        seen.add((i, j))
        if not (helper(i-1, j, idx+1) or helper(i+1, j, idx+1) or helper(i, j-1, idx+1) or helper(i, j+1, idx+1)):
            seen.remove((i, j))
            return False

        return True

    HEIGHT = len(board)
    WIDTH = len(board[0])
    seen = set()
    # For every first character of a wanted target, check recursively whether we can make the rest of the target
    return any(helper(i, j, 0) for i in range(HEIGHT)
               for j in range(WIDTH) if board[i][j] == target[0])


@time_execution()
def sol_rec_v3(board: list[list[str]], target: str) -> bool:
    def helper(i: int, j: int, idx: int) -> bool:
        if idx == len(target):
            return True
        # Out of bounds, found a character that doesn't match or already used this char
        if i == -1 or i == HEIGHT or j == -1 or j == WIDTH or board[i][j] != target[idx] or seen[i][j]:
            return False

        # Go in all directions, and remove from seen if this path ended up being false
        seen[i][j] = True
        if not (helper(i-1, j, idx+1) or helper(i+1, j, idx+1) or helper(i, j-1, idx+1) or helper(i, j+1, idx+1)):
            seen[i][j] = False
            return False

        return True

    HEIGHT = len(board)
    WIDTH = len(board[0])
    seen = [[False]*WIDTH for _ in range(HEIGHT)]
    # For every first character of a wanted target, check recursively whether we can make the rest of the target
    return any(helper(i, j, 0) for i in range(HEIGHT)
               for j in range(WIDTH) if board[i][j] == target[0])


@time_execution()
def sol_rec_v4(board: list[list[str]], target: str) -> bool:
    HEIGHT = len(board)
    WIDTH = len(board[0])

    # There is too little characters overall
    if len(target) > HEIGHT*WIDTH:
        return False

    # Count of some of the characters is too little
    char_count = Counter(sum(board, []))
    for char, count in Counter(target).items():
        if char_count[char] < count:
            return False

    # If there's more letters in the board that the target starts with then reverse it, we will start looking from back instead
    if char_count[target[0]] > char_count[target[-1]]:
        target = target[::-1]

    def helper(i: int, j: int, idx: int):
        if idx == len(target):
            return True
        # Out of bounds, characters don't match, or been here before
        if i == -1 or j == -1 or i == HEIGHT or j == WIDTH or target[idx] != board[i][j] or (i, j) in seen:
            return False

        # Go in all directions, and remove from seen if this path ended up being false
        seen.add((i, j))
        if not (helper(i-1, j, idx+1) or helper(i+1, j, idx+1) or helper(i, j-1, idx+1) or helper(i, j+1, idx+1)):
            seen.remove((i, j))
            return False

        return True

    seen = set()
    return any(helper(i, j, 0) for i in range(HEIGHT)
               for j in range(WIDTH) if board[i][j] == target[0])


@time_execution()
def sol_rec_v5(board: list[list[str]], target: str) -> bool:
    HEIGHT = len(board)
    WIDTH = len(board[0])

    # There is too little characters overall
    if len(target) > HEIGHT*WIDTH:
        return False

    # Count of some of the characters is too little
    char_count = Counter(sum(board, []))
    for char, count in Counter(target).items():
        if char_count[char] < count:
            return False

    # If there's more letters in the board that the target starts with then reverse it, we will start looking from back instead
    if char_count[target[0]] > char_count[target[-1]]:
        target = target[::-1]

    def helper(i: int, j: int, idx: int):
        if idx == len(target):
            return True
        # Out of bounds, characters don't match, or been here before
        if i < 0 or j < 0 or i == HEIGHT or j == WIDTH or target[idx] != board[i][j] or seen[i][j]:
            return False

        # Go in all directions, and remove from seen if this path ended up being false
        seen[i][j] = True
        if not (helper(i-1, j, idx+1) or helper(i+1, j, idx+1) or helper(i, j-1, idx+1) or helper(i, j+1, idx+1)):
            seen[i][j] = False
            return False

        return True

    seen = [[False]*WIDTH for _ in range(HEIGHT)]
    return any(helper(i, j, 0) for i in range(HEIGHT)
               for j in range(WIDTH) if board[i][j] == target[0])
