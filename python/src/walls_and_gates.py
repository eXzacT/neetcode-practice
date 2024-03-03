from collections import deque
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an m x n grid 'rooms' initialized with three possible values:

        -1 -> a wall or an obstacle
        0 -> a gate
        Infinity -> empty room, we represent infinity as 2^31-1=2147483647
        
    Fill each empty room with the distance to its closest gate, if the gate can't be reached it should be filled with Infinity.'''


@time_execution(executions=1)
def sol_bfs(rooms: list[list[int]]) -> list[list[int]]:
    WIDTH = len(rooms[0])
    HEIGHT = len(rooms)

    # Start bfs from every position where there's a gate
    queue = deque([(i, j) for i in range(HEIGHT)
                  for j in range(WIDTH) if rooms[i][j] == 0])
    dist = 0

    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()

            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                # In bounds and an empty room, meaning we can go through it
                if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and rooms[ni][nj] == 2147483647:
                    rooms[ni][nj] = dist+1  # We reached this room with dist
                    queue.append((ni, nj))

        dist += 1

    return rooms
