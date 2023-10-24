def rooms_needed(tuples: list) -> bool:
    """ Checks how many rooms are needed, no overlap. 2023-10-24 16:21:53 """
    rooms_needed=1
    j=0
    sorted_by_start = sorted(item[0] for item in tuples)
    sorted_by_end = sorted(item[1] for item in tuples)
    
    for i in range(len(sorted_by_start)-1):
        if sorted_by_start[i]==sorted_by_start[i+1]: # all meetings that start at the same time need a room 2023-10-24 16:49:54
            rooms_needed+=1
        else: # otherwise check if one of the meetings ended 2023-10-24 16:50:52
            # this means one of the rooms is now free 2023-10-24 16:06:25
            if sorted_by_start [i+1]>=sorted_by_end[j]:
                j+=1 # every time we compare to the smallest, make the next one smallest 2023-10-24 16:20:07
                continue
            else:
                rooms_needed+=1
    return rooms_needed # returns True if there are no overlaps 2023-10-24 15:01:10