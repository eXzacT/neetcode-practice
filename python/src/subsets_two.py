if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


''' Given an integer array nums that may contain duplicates, return all possible subsets(the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.'''


@time_execution()
def sol_naive(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    subsets = set()

    def helper(i: int, subset: list[int]) -> None:
        if i == len(nums):
            subsets.add(tuple(subset))
            return

        subsets.add(tuple(subset))
        for j in range(i, len(nums)):
            subset.append(nums[j])
            helper(j+1, subset)
            subset.pop()

    helper(0, [])
    return [list(subset) for subset in subsets]


@time_execution()
def sol_optimized(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    subsets = []

    def helper(i: int, subset: list[int] = []) -> None:
        if i == len(nums):
            subsets.append(subset)
            return

        # Take
        helper(i+1, subset+[nums[i]])
        # Don't take, but also don't take any value that's same as the one we didn't take
        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1

        helper(i+1, subset)

    helper(0)
    return subsets


@time_execution()
def sol_optimized_v2(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    subsets = []
    subset = []

    def helper(i: int) -> None:
        if i == len(nums):
            subsets.append(subset[:])
            return

        subset.append(nums[i])
        helper(i+1)

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        subset.pop()
        helper(i+1)

    helper(0)
    return subsets


@time_execution()
def sol_optimized_v3(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    subsets = []

    def helper(i: int, subset: list[int]) -> None:
        subsets.append(subset[:])
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            subset.append(nums[j])
            helper(j + 1, subset)
            subset.pop()

    helper(0, [])
    return subsets


@time_execution()
def sol_optimized_v4(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    subsets = []

    def helper(i: int, subset: list[int] = []) -> None:
        subsets.append(subset[:])
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            helper(j + 1, subset+[nums[j]])

    helper(0)
    return subsets
