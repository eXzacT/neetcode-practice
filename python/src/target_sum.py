if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''You are given an integer array nums and an integer target.
    You want to build an expression out of nums by adding one of the symbols '+' and '-' 
    before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 
    and concatenate them to build the expression "+2-1".

    Return the number of different expressions that you can build, which evaluates to target.'''


@time_execution()
def sol_dp(nums: list[int], target: int) -> int:
    total_sum = sum(nums)
    if not (-1*total_sum <= target <= total_sum):
        return 0
    dp = [[0 for _ in range(total_sum*2 + 1)] for _ in range(len(nums))]

    # We pretend total sum is 0 since it's the middle
    # Left part of the table represents going into negative space, right side going into positive
    dp[0][total_sum + nums[0]] += 1
    dp[0][total_sum - nums[0]] += 1

    # Create branches for the rest of rows
    for i in range(1, len(nums)):
        for j in range(total_sum*2 + 1):
            # Populate left part of the tree
            if (j - nums[i] >= 0 and dp[i-1][j-nums[i]] > 0):
                dp[i][j] += dp[i-1][j-nums[i]]

            # Populate right part of the tree
            if (j + nums[i] <= total_sum*2 and dp[i-1][j+nums[i]] > 0):
                dp[i][j] += dp[i-1][j+nums[i]]

    # Result is in the last row, and target is distance from the middle(total sum)
    return dp[-1][total_sum + target]


@time_execution()
def sol_dp_v2(nums: list[int], target: int) -> int:
    nums_sum = sum(nums)
    if nums_sum < abs(target) or (target+nums_sum) % 2 != 0:
        return 0
    else:
        sum_p = (target+nums_sum)//2

    dp = [0]*(sum_p+1)
    dp[0] = 1
    for num in nums:
        for i in range(sum_p, num-1, -1):
            dp[i] = dp[i]+dp[i-num]

    return dp[sum_p]


@time_execution()
def sol_rec(nums: list[int], target: int) -> int:
    def helper(i: int, remainder: int) -> int:
        if i == len(nums):
            return remainder == 0

        return helper(i+1, remainder-nums[i])+helper(i+1, remainder+nums[i])

    return helper(0, target)


@time_execution()
def sol_memo(nums: list[int], target: int) -> int:
    memo = {}

    def helper(i: int, remainder: int) -> int:
        if i == len(nums):
            return remainder == 0
        key = (i, remainder)
        if key in memo:
            return memo[key]

        memo[key] = helper(i+1, remainder-nums[i]) + \
            helper(i+1, remainder+nums[i])
        return memo[key]

    return helper(0, target)
