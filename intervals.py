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


def count_overlaping_intervals(intervals):

    intervals.sort(key=lambda x: x[0])
    intervals_and_its_overlaps = {}
    counter = 0

    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            # If there is an overlap (27/10/2023)
            if intervals[i][1] <= intervals[j][0]:
                break
            else:
                # Convert lists to tuples because lists are unhashable
                current_interval = tuple(intervals[i])
                overlaping_interval = tuple(intervals[j])

                # Add the interval as a key to the dictionary and add all the overlapping intervals to it (27/10/2023)
                if current_interval not in intervals_and_its_overlaps:
                    intervals_and_its_overlaps[current_interval] = []
                intervals_and_its_overlaps[current_interval].append(
                    overlaping_interval)

                # Add all the overlapping intervals as keys to the dictionary and add the current interval as a value to them (27/10/2023)
                if overlaping_interval not in intervals_and_its_overlaps:
                    intervals_and_its_overlaps[overlaping_interval] = []
                intervals_and_its_overlaps[overlaping_interval].append(
                    current_interval)

    while intervals_and_its_overlaps:
        # Find the interval with most overlaps and delete it (27/10/2023)
        # If there are more intervals with same amount of overlaps then pick the shorter length (27/10/2023)
        max_key = max(intervals_and_its_overlaps, key=lambda k: (
            len(intervals_and_its_overlaps[k]), -(k[1]-k[0])))
        if (max_key):
            counter += 1
        del (intervals_and_its_overlaps[max_key])

        # Recreate the values of each other interval so they don't include the deleted interval (27/10/2023)
        def remove_max_key_from_values_of_other_keys(overlaps): return [
            overlap for overlap in overlaps if overlap != max_key]
        for key in intervals_and_its_overlaps:
            intervals_and_its_overlaps[key] = remove_max_key_from_values_of_other_keys(
                intervals_and_its_overlaps[key])

        # If there are no overlaps left, break the loop
        if not any(intervals_and_its_overlaps.values()):
            break

    return counter
