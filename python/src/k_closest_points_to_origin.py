from heapq import heapify, heappop
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).'''


@time_execution()
def sol_naive(points: list[list[int, int]], k: int) -> list[list[int, int]]:
    dists = []
    for x, y in points:
        dists.append([x**2 + y**2, x, y])

    return [[x, y] for _, x, y in sorted(dists)[:k]]


@time_execution()
def sol_optimized(points: list[list[int, int]], k: int) -> list[list[int, int]]:
    heap = [[x**2 + y**2, x, y] for x, y in points]
    heapify(heap)

    return [heappop(heap)[1:] for _ in range(k)]
