if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an array of meeting time intervals consisting of start and end times, 
    find the minimum number of conference room needed for all the meetings to be held'''


@time_execution()
def sol(meetings: list[list[int, int]]) -> int:
    meetings = sorted(meetings)
    rooms = [meetings[0][1]]

    for i in range(1, len(meetings)):
        start, end = meetings[i]
        # No overlap, we can take over the same room but update the end time
        if rooms[0] <= start:
            rooms[0] = end
        else:  # Allocate a new room
            rooms.append(end)

        rooms.sort()  # Keep it sorted by end times

    return len(rooms)


@time_execution()
def sol_v2(meetings: list[list[int, int]]) -> int:
    starts = sorted([meeting[0] for meeting in meetings])
    ends = sorted([meeting[1] for meeting in meetings])
    count = max_count = 0

    i = j = 0
    while i < len(starts):
        if starts[i] < ends[j]:  # Keep adding rooms while none of the meetings have ended yet
            count += 1
            i += 1
        else:  # Some rooms have freed up
            count -= 1
            j += 1

        max_count = max(count, max_count)

    return max_count
