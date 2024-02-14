from collections import deque
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an array of integers nums, there is a sliding window of size k 
    which is moving from the very left of the array to the very right.  
    You can only see the k numbers in the window. Each time the sliding window moves right by one position.
    Return the max sliding window.'''


@time_execution()
def sol_naive(nums: list[int], k: int) -> list[int]:
    return [max(nums[i:i+k]) for i in range(0, len(nums)-k+1)]


@time_execution()
def sol_optimized(nums: list[int], k: int) -> list[int]:
    queue = deque([nums[0]])
    for i in range(1, k):
        while queue and queue[-1] < nums[i]:
            queue.pop()
        queue.append(nums[i])

    l, r = 0, k-1
    res = [queue[0]]
    while r < len(nums)-1:
        if queue[0] == nums[l]:  # If the leftmost number in the queue is also the leftmost in the window
            queue.popleft()

        # Slide the window and keep it in a decreasing order
        r += 1
        l += 1
        while queue and queue[-1] < nums[r]:
            queue.pop()

        queue.append(nums[r])
        # Whichever number is at 0th position when this is done is also max in window
        res.append(queue[0])

    return res
