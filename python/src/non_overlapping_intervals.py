if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an array of intervals intervals where intervals[i] = [starti, endi], 
    return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.'''


@time_execution()
def sol(intervals: list[list[int, int]]) -> int:
    intervals = sorted(intervals)
    prev = intervals[0]
    res = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] < prev[1]:  # Overlap, HAVE to kick one of the intervals
            if intervals[i][1] < prev[1]:  # Kick the previous interval since it's longer
                prev = intervals[i]
            res += 1
        else:  # No overlap, means we now have to compare to the current interval
            prev = intervals[i]

    return res


@time_execution()
def sol_optimized(intervals: list[list[int, int]]) -> int:
    intervals = sorted(intervals, key=lambda x: x[1])
    kept = 1
    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] >= prev_end:
            prev_end = intervals[i][1]
            kept += 1

    return len(intervals)-kept
