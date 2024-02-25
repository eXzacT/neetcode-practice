if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. 
    You are asked to burst all the balloons.
    If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. 
    If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
    Return the maximum coins you can collect by bursting the balloons wisely.'''


@time_execution()
def sol_dp(nums: list[int]) -> int:
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for r in range(2, n):
        for l in range(r - 2, -1, -1):
            dp[l][r] = max(nums[l]*nums[r]*nums[m] + dp[l][m] + dp[m][r]
                           for m in range(l + 1, r))

    return dp[0][n-1]


@time_execution()
def sol_rec(nums: list[int]) -> int:
    def helper(nums: list[int]) -> int:
        if len(nums) == 2:
            return nums[0]*nums[1]+max(nums)

        max_value = 0
        for i in range(len(nums)):
            left = 1 if i == 0 else nums[i-1]
            right = 1 if i == len(nums)-1 else nums[i+1]

            pop_current = left*right*nums[i]
            rest = helper(nums[:i]+nums[i+1:])
            max_value = max(max_value, pop_current+rest)

        return max_value

    return helper(nums)


@time_execution()
def sol_memo(nums: list[int]) -> int:
    memo = {}

    def helper(nums: list[int]) -> int:
        key = tuple(nums)
        if key in memo:
            return memo[key]
        if len(nums) == 2:
            return nums[0]*nums[1]+max(nums)

        max_value = 0
        for i in range(len(nums)):
            left = 1 if i == 0 else nums[i-1]
            right = 1 if i == len(nums)-1 else nums[i+1]

            pop_current = left*right*nums[i]
            rest = helper(nums[:i]+nums[i+1:])
            max_value = max(max_value, pop_current+rest)

        memo[key] = max_value
        return max_value

    return helper(nums)


@time_execution()
def sol_rec_v2(nums: list[int]) -> int:
    def helper(left: int, right: int) -> int:
        if left > right:
            return 0

        max_value = 0
        for i in range(left, right+1):
            pop_current_last = nums[left-1]*nums[i]*nums[right+1]
            res = helper(left, i-1)+pop_current_last+helper(i+1, right)
            max_value = max(max_value, res)

        return max_value

    nums = [1]+nums+[1]
    return helper(1, len(nums)-2)


@time_execution()
def sol_memo_v2(nums: list[int]) -> int:
    memo = {}

    def helper(left: int, right: int) -> int:
        if left > right:
            return 0
        key = (left, right)
        if key in memo:
            return memo[key]

        max_value = 0
        for i in range(left, right+1):
            pop_current_last = nums[left-1]*nums[i]*nums[right+1]
            res = helper(left, i-1)+pop_current_last+helper(i+1, right)
            max_value = max(max_value, res)

        memo[key] = max_value
        return max_value

    nums = [1]+nums+[1]
    return helper(1, len(nums)-2)


@time_execution()
def sol_memo_v3(nums: list[int]) -> int:
    memo = [[0]*(len(nums)+1) for _ in range(len(nums)+1)]

    def helper(left: int, right: int) -> int:
        if left > right:
            return 0
        if memo[left][right]:
            return memo[left][right]

        max_value = 0
        for i in range(left, right+1):
            pop_current_last = nums[left-1]*nums[i]*nums[right+1]
            res = helper(left, i-1)+pop_current_last+helper(i+1, right)
            max_value = max(max_value, res)

        memo[left][right] = max_value
        return max_value

    nums = [1]+nums+[1]
    return helper(1, len(nums)-2)
