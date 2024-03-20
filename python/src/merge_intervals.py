if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
    and return an array of the non-overlapping intervals that cover all the intervals in the input.'''


@time_execution()
def sol(intervals: list[list[int, int]]) -> list[list[int, int]]:
    def overlap(a: list[int, int], b: list[int, int]):
        return a[1] >= b[0]

    # Sort the intervals by start
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if not overlap(merged[-1], intervals[i]):
            merged.append(intervals[i])
        else:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])

    return merged
