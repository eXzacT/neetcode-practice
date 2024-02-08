if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.'''


@time_execution()
def sol(nums: list[int]) -> list[list[int]]:
    def helper(idx: int = 0, subset: list[int] = []) -> None:
        if idx == len(nums):
            subsets.append(subset)
            return

        helper(idx+1, subset)  # Without
        helper(idx+1, subset+[nums[idx]])  # With

    subsets = []
    helper()
    return subsets


@time_execution()
def sol_v2(nums: list[int]) -> list[list[int]]:
    def helper(idx: int = 0, subset: list[int] = []) -> None:
        subsets.append(subset)
        for i in range(idx, len(nums)):
            helper(i+1, subset+[nums[i]])

    subsets = []
    helper()
    return subsets


@time_execution()
def sol_v3(nums: list[int]) -> list[list[int]]:
    def helper(idx: int = 0) -> list[list[int]]:
        if idx == len(nums):
            return [[]]

        subsets = []
        for subset in helper(idx + 1):
            subsets.append(subset)
            subsets.append([nums[idx]] + subset)

        return subsets

    return helper()


@time_execution()
def sol_v4(nums: list[int]) -> list[list[int]]:
    def helper(idx: int = 0) -> None:
        if idx == len(nums):
            subsets.append(subset.copy())
            return

        # Include the current number in the subset
        subset.append(nums[idx])
        helper(idx + 1)
        subset.pop()  # Remove the current number from the subset

        # Exclude the current number from the subset
        helper(idx + 1)

    subset = []
    subsets = []
    helper()
    return subsets
