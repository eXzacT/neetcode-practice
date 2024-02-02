from itertools import combinations
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.'''


@time_execution()
def sol_naive(nums: int) -> list[list[int]]:
    res = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] == 0:
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))

    return sorted([list(x) for x in res])


@time_execution()
def sol_naive_functional(nums: int) -> list[list[int]]:
    return sorted([list(x) for x in set(tuple(sorted(comb)) for comb in combinations(nums, 3) if sum(comb) == 0)])


@time_execution()
def sol_optimized(nums: int) -> list[list[int]]:
    nums = sorted(nums)
    res = []

    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            left = i+1
            right = len(nums)-1
            while left < right:
                three_sum = nums[left]+nums[right]+nums[i]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # Keep skipping the same number
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

    return res
