if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
    There is only one repeated number in nums, return this repeated number.
    You must solve the problem without modifying the array nums and uses only constant extra space.'''


@time_execution()
def sol_naive(nums: list[int]) -> int:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return nums[i]


@time_execution()
def sol_floyd_cycle_detection(nums: list[int]) -> int:
    slow = fast = 0
    while True:
        slow = nums[slow]  # [1,3,4,2,2], index 0 -> 1, 1 jump
        fast = nums[nums[fast]]  # index 0->1, 1->3, 2 jumps

        if nums[slow] == nums[fast]:  # Reached the last node of a cycle
            break

    # Keep the initial slow as it is and initialize another slow from the beginning, where they meet is the result
    slow2 = 0
    while nums[slow] != nums[slow2]:
        slow = nums[slow]
        slow2 = nums[slow2]

    return nums[slow]
