if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. 
    Each cycle or interval allows the completion of one task. 
    Tasks can be completed in any order, but there's a constraint: 
        identical tasks must be separated by at least n intervals due to cooling time.
    Return the minimum number of intervals required to complete all tasks.'''

from heapq import heappop, heappush, heapify
from collections import deque


@time_execution()
def sol_heap(tasks: list[str], n: int) -> int:
    occurences = {}

    for task in tasks:
        occurences[task] = occurences.get(task, 0) + 1

    heap = [-c for c in occurences.values()]
    heapify(heap)

    time = 0
    queue = deque()
    while heap or queue:
        time += 1
        if heap:
            count = heappop(heap)+1
            if count < 0:
                # When can we process this task again?
                queue.append([count, time+n])
        # Ready to process because 'n' time has passed since last
        if queue and queue[0][1] == time:
            heappush(heap, queue.popleft()[0])

    return time


@time_execution()
def sol_optimized(tasks: list[str], n: int) -> int:
    task_counts = {}
    for task in tasks:
        task_counts[task] = task_counts.get(task, 0) + 1

    max_occurence = max(task_counts.values())
    tasks_with_max_occurrences = sum(1 for count in task_counts.values()
                                     if count == max_occurence)

    min_time_needed = (max_occurence - 1) * (n + 1) + \
        tasks_with_max_occurrences

    return max(min_time_needed, len(tasks))
