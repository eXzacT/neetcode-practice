'''Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.'''

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


@time_execution()
def contains_duplicate_naive(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


@time_execution()
def contains_duplicate_optimized(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)


@time_execution()
def contains_duplicate_optimized_v2(nums: list[int]) -> bool:
    nums_set = set()
    for num in nums:
        if num in nums_set:
            return True
        nums_set.add(num)

    return False
