if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
    represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
    You are also given an interval new_interval = [start, end] that represents the start and end of another interval.
    Insert new_interval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
    Return intervals after the insertion.
    Note that you don't need to modify intervals in-place. You can make a new array and return it.'''


@time_execution()
def sol(intervals: list[list[int, int]], new_interval: list[int, int]) -> list[list[int, int]]:
    res = []

    for i in range(len(intervals)):
        if new_interval[1] < intervals[i][0]:
            res.append(new_interval)
            return res+intervals[i:]
        elif new_interval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            new_interval = [min(intervals[i][0], new_interval[0]),
                            max(intervals[i][1], new_interval[1])]

    res.append(new_interval)

    return res


@time_execution()
def sol_v2(intervals: list[list[int, int]], new_interval: list[int, int]) -> list[list[int, int]]:
    n = len(intervals)
    i = 0
    res = []

    # Keep adding the intervals as long as they end before the new interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1

    # Intervals overlap,keep extending it until they stop overlapping
    while i < n and new_interval[1] >= intervals[i][0]:
        new_interval = [min(new_interval[0], intervals[i][0]),
                        max(new_interval[1], intervals[i][1])]
        i += 1

    res.append(new_interval)

    # Add the rest since they happen after new interval
    while i < n:
        res.append(intervals[i])
        i += 1

    return res
