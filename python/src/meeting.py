def min_meeting_rooms(tuples: list) -> bool:
    """ Checks how many rooms are needed,so the meetings don't overlap (24/10/2023) """
    rooms_needed = 1
    j = 0
    sorted_by_start = sorted(item[0] for item in tuples)
    sorted_by_end = sorted(item[1] for item in tuples)

    for i in range(len(sorted_by_start)-1):
        # all meetings that start at the same time need a room
        if sorted_by_start[i] == sorted_by_start[i+1]:
            rooms_needed += 1
        else:  # otherwise check if one of the meetings ended
            # this means one of the rooms is now free
            if sorted_by_start[i+1] >= sorted_by_end[j]:
                j += 1  # every time we compare to the smallest, make the next one smallest
                continue
            else:
                rooms_needed += 1
    return rooms_needed  # returns True if there are no overlaps
