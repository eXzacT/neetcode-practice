if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an array nums containing n distinct numbers in the range [0, n], 
    return the only number in the range that is missing from the array.'''


@time_execution()
def sol_formula(nums: list[int]) -> int:
    return (len(nums)*(len(nums)+1))//2-sum(nums)


@time_execution()
def sol_sort(nums: list[int]) -> int:
    nums = sorted(nums)
    for i in range(len(nums)+1):
        if i == len(nums) or i != nums[i]:
            return i


@time_execution()
def sol_binary(nums: list[int]) -> int:
    res = 0
    for i in range(len(nums)):
        res ^= i+1
        res ^= nums[i]
    return res
