if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


@time_execution()
def two_sum_naive(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i, j]


@time_execution()
def two_sum_optimized(nums: list[int], target: int) -> list[int]:
    nums_dict = {}
    for idx, num in enumerate(nums):
        if num in nums_dict:
            return [nums_dict[num], idx]
        nums_dict[target-num] = idx
