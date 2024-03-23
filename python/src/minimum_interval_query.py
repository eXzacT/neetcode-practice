from heapq import heappush, heappop

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given a 2D integer array intervals, the interval goes from starti to endi(inclusive).
    You are also given an integer array queries. You have to return the length of the smallest interval that contains the number from the query, if there is no such interval then return -1.
    Return an array containing the answers to the queries.'''


@time_execution()
def sol_naive(intervals: list[list[int, int]], queries: list[int]) -> list[int]:
    intervals = sorted(intervals)

    def find_smallest_interval(query: int) -> int:
        smallest_interval = float('inf')
        for interval in intervals:
            if interval[0] <= query <= interval[1]:
                smallest_interval = min(
                    smallest_interval, interval[1] - interval[0] + 1)

            if interval[0] > query:  # Can't possibly find an interval where query is present
                break

        return -1 if smallest_interval == float('inf') else smallest_interval

    return [find_smallest_interval(query) for query in queries]


@time_execution()
def sol_naive_v2(intervals: list[list[int, int]], queries: list[int]) -> list[int]:
    size = {}
    for interval in intervals:
        for i in range(interval[0], interval[1] + 1):
            if i not in size:
                size[i] = interval[1] - interval[0] + 1
            else:
                size[i] = min(size[i], interval[1] - interval[0] + 1)

    return [size.get(query, -1) for query in queries]


@time_execution()
def sol_optimized(intervals: list[list[int, int]], queries: list[int]) -> list[int]:
    intervals = sorted(intervals)
    queries = sorted([(query, i) for i, query in enumerate(queries)])
    size = [-1]*len(queries)
    heap = []
    i = 0

    for query in queries:
        # Keep adding intervals to the heap that the query belongs to
        while i < len(intervals) and intervals[i][0] <= query[0]:
            l, r = intervals[i]
            if r >= query[0]:
                heappush(heap, (r-l+1, r))  # (size,end)
            i += 1

        # Remove intervals that are too far to the left for the query to belong to
        while heap and heap[0][1] < query[0]:
            heappop(heap)

        if heap:  # Does the query belong to any interval?
            # query[1] is the index of the query in the original list of queries
            # Size of the smallest interval the query belongs to
            size[query[1]] = heap[0][0]

    return size


@time_execution()
def sol_optimized_v2(intervals: list[list[int, int]], queries: list[int]) -> list[int]:
    intervals = sorted(intervals, reverse=True)
    heap = []
    size = {}

    for query in sorted(queries):
        # Keep adding intervals to the heap that the query belongs to
        while intervals and intervals[-1][0] <= query:
            l, r = intervals.pop()
            if r >= query:  # Only add it if the query belongs to the interval
                heappush(heap, (r-l+1, r))  # (size,end)

        # Remove intervals that are too far to the left for the query to belong to
        while heap and heap[0][1] < query:
            heappop(heap)

        size[query] = heap[0][0] if heap else -1

    return [size[query] for query in queries]
