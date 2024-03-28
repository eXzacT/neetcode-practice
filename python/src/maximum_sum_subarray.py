if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum. '''


@time_execution()
def sol_naive(nums: list[int]) -> int:
    return max([sum(nums[i:j]) for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)])


@time_execution()
def sol_quadratic(nums: list[int]) -> int:
    max_sum = nums[0]

    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)

    return max_sum


@time_execution()
def sol_dp(nums: list[int]) -> int:
    curr_with = curr_without = nums[0]

    for i in range(1, len(nums)):
        # Should we start a new subarray or continue the current one?
        curr_with = max(nums[i], curr_with + nums[i])
        curr_without = max(curr_with, curr_without)

    return max(curr_with, curr_without)


@time_execution()
def sol_sliding(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0  # Start a new subarray
        curr_sum += num
        max_sum = max(max_sum, curr_sum)

    return max_sum
