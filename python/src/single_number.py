if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.'''


@time_execution()
def sol_naive(nums: list[int]) -> int:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                break
        else:
            return nums[i]


@time_execution()
def sol_time_optimized(nums: list[int]) -> int:
    num_count = {}
    for num in nums:
        num_count[num] = num_count.get(num, 0)+1

    return [num for num in num_count if num_count[num] == 1][0]


@time_execution()
def sol_time_optimized_v2(nums: list[int]) -> int:
    nums_set = set()
    for num in nums:
        if num in nums_set:
            nums_set.remove(num)
        else:
            nums_set.add(num)

    return nums_set.pop()


@time_execution()
def sol_space_time_optimized(nums: list[int]) -> int:
    state = 0
    for num in nums:
        state ^= num

    return state
