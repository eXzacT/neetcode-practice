from itertools import groupby

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.'''


@time_execution()
def sol_naive(nums: list[int]) -> int:
    sol = 0
    for i in range(len(nums)):
        max_len = 1
        curr = nums[i]+1
        j = 0
        while j < len(nums):
            if nums[j] == curr:
                max_len += 1
                curr += 1
                j = 0
            j += 1

        sol = max(max_len, sol)

    return sol


@time_execution()
def sol_sorted(nums: list[int]) -> int:
    if not nums:
        return 0

    nums = sorted(nums)

    prev_max_len = 0
    max_len = 0

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]+1:
            max_len += 1
        else:
            prev_max_len = max(max_len, prev_max_len)
            max_len = 0

    return 1+max(max_len, prev_max_len)


@time_execution()
def sol_sorted_groupby(nums: list[int]) -> int:
    return max((len(list(g)) for _, g in groupby(enumerate(sorted(nums)), lambda i_x: i_x[0]-i_x[1])), default=0)


@time_execution()
def sol_optimized(nums: list[int]) -> int:
    nums_set = set(nums)
    max_len = 0
    for num in nums:
        if num-1 not in nums_set:  # Current number is the leftmost number in a sequence
            curr_len = 0
            # Count the current sequence length and update max if max
            while num+curr_len in nums_set:
                curr_len += 1
            max_len = max(curr_len, max_len)

    return max_len


print(sol_optimized([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
