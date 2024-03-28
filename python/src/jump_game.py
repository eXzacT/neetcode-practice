if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
    Return true if you can reach the last index, or false otherwise.'''


@time_execution()
def sol_naive(nums: list[int]) -> bool:
    def helper(pos: int) -> bool:
        if pos >= len(nums):
            return False
        if pos == len(nums)-1:
            return True

        return any(helper(pos+jump) for jump in range(1, nums[pos]+1))

    return helper(0)


@time_execution()
def sol_memo(nums: list[int]) -> bool:
    memo = {len(nums)-1: True}

    def helper(pos: int) -> bool:
        if pos in memo:
            return memo[pos]
        if pos >= len(nums):
            return False

        memo[pos] = any(helper(pos+jump) for jump in range(1, nums[pos]+1))
        return memo[pos]

    return helper(0)


@time_execution()
def sol_memo_v2(nums: list[int]) -> bool:
    memo = [None]*len(nums)

    def helper(pos: int) -> bool:
        if memo[pos] != None:
            return memo[pos]
        if pos == len(nums)-1:
            return True
        if pos >= len(nums):
            return False

        memo[pos] = any(helper(pos+jump) for jump in range(1, nums[pos]+1))
        return memo[pos]

    return helper(0)


@time_execution()
def sol_dp(nums: list[int]) -> bool:
    n = len(nums)
    if len(nums) == 1:
        return True

    dp = [False]*n
    dp[0] = True

    for i in range(n):
        if dp[i]:
            for j in range(1, nums[i]+1):
                if i+j == n-1:
                    return True
                if i+j < n:
                    dp[i+j] = True

    return False


@time_execution()
def sol_greedy(nums: list[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0
