def insert_into_intervals(intervals, new_interval):
    res = []
    i = 0
    intervals.sort(key=lambda x: x[0])
    while (i < len(intervals)):

        # Append all the intervals that are happening before the new interval and don't overlap (25/10/2023)
        if intervals[i][1] < new_interval[0]:
            res.append(intervals[i])
            i += 1
            continue
        # Merge intervals that overlap with new_interval (25/10/2023)
        if intervals[i][0] <= new_interval[1]:
            new_interval = [min(new_interval[0], intervals[i][0]),
                            max(new_interval[1], intervals[i][1])]
            i += 1
            continue
        # If there was no overlaps or new interval happens before the intervals (25/10/2023)
        break

    res.append(new_interval)

    while (i < len(intervals)):
        # Append all the other intervals that come after the new interval if there are any (25/10/2023)
        res.append(intervals[i])
        i += 1

    return res


def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals:
        # Get the ending point of the last element in the result list (26/10/2023)
        lastEnd = merged[-1][1]

        # If the current interval overlaps with the last interval in the result list, merge them (26/10/2023)
        if start <= lastEnd:
            # [1,3][2,4] becomes [1,4] (26/10/2023)
            merged[-1][1] = max(lastEnd, end)
        else:
            # If not, add the current interval to the result list (26/10/2023)
            merged.append([start, end])

    return merged
