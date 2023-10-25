def insert_into_intervals(intervals, new_interval):
    res = []
    i = 0

    while (i < len(intervals)):

        # Append all the intervals that are happening before the new interval and don't overlap 2023-10-25 17:05:34
        if intervals[i][1] < new_interval[0]:
            res.append(intervals[i])
            i += 1
            continue
        # Merge intervals that overlap with new_interval 2023-10-25 17:06:40
        if intervals[i][0] <= new_interval[1]:
            new_interval = [min(new_interval[0], intervals[i][0]),
                            max(new_interval[1], intervals[i][1])]
            i += 1
            continue
        break  # break once you set the new interval 2023-10-25 17:36:42

    res.append(new_interval)

    while (i < len(intervals)):
        # Append all the other intervals that come after the new interval, but are still in the intervals 2023-10-25 17:06:59
        res.append(intervals[i])
        i += 1

    return res
