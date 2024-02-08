from itertools import permutations

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.'''


@time_execution()
def sol_builtin(nums: list[int]) -> list[list[int]]:
    return [list(p) for p in permutations(nums, len(nums))]


@time_execution()
def sol_naive(nums: list[int]) -> list[list[int]]:
    def helper(permutation: list[int] = []) -> None:
        if len(permutation) == len(nums):
            permutations.append(permutation)
            return

        for num in nums:
            if num not in permutation:
                helper(permutation + [num])

    permutations = []
    helper()
    return permutations


@time_execution()
def sol_set(nums: list[int]) -> list[list[int]]:
    def helper(permutation: list[int] = []) -> None:
        if len(permutation) == len(nums):
            permutations.append(permutation)
            return

        for num in nums:
            if num not in used:
                used.add(num)
                helper(permutation + [num])
                used.remove(num)

    permutations = []
    used = set()
    helper()
    return permutations


@time_execution()
def sol_set_v2(nums: list[int]) -> list[list[int]]:
    def helper(permutation: list[int] = []) -> None:
        if len(permutation) == len(nums):
            permutations.append(permutation)
            return

        for i in range(len(nums)):
            if i not in used:
                used.add(i)
                helper(permutation + [nums[i]])
                used.remove(i)

    permutations = []
    used = set()
    helper()
    return permutations


@time_execution()
def sol_v3(nums: list[int]) -> list[list[int]]:
    def helper(permutation: list[int]) -> list[list[int]]:
        if len(permutation) == 1:
            return [permutation]

        permutations = []
        for i in range(len(permutation)):
            rest = permutation[:i] + permutation[i+1:]
            for p in helper(rest):
                permutations.append([permutation[i]] + p)

        return permutations

    return helper(nums)


@time_execution()
def sol_v4(nums: list[int]) -> list[list[int]]:
    def helper(permutation: list[int]) -> list[int]:
        if len(permutation) == 1:
            return [permutation[:]]

        permutations = []
        for _ in range(len(permutation)):
            num = permutation.pop(0)
            perms = helper(permutation)
            for perm in perms:
                perm.append(num)

            permutations.extend(perms)
            permutation.append(num)

        return permutations

    return helper(nums)


@time_execution()
def sol_v5(nums: list[int]) -> list[list[int]]:
    def helper(start: int):
        if start == len(nums) - 1:
            permutations.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[i], nums[start] = nums[start], nums[i]  # Swap elements
            helper(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Backtrack

    permutations = []
    helper(0)
    return permutations
