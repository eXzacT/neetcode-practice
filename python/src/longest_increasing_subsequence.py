import bisect
import networkx as nx
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an integer array nums, return the length of the longest strictly increasing subsequence'''


@time_execution()
def sol_dp(nums: list[int]) -> int:
    dp = [0]*len(nums)
    dp[0] = 1  # Longest increasing sequence of one num is the number itself

    for i in range(1, len(nums)):
        # We could have gotten here from any numbers before current if they were smaller than current
        dp[i] = 1+max([dp[j]
                       for j in range(i) if nums[i] > nums[j]], default=0)

    return max(dp)


@time_execution()
def sol(nums: list[int]) -> int:
    def helper(i: int, prev: int = float('-inf')) -> int:
        if i == len(nums):
            return 0

        # If we can take the current, split into two paths, where we take and where we don't take
        if nums[i] > prev:
            return max(1+helper(i+1, nums[i]), helper(i+1, prev))
        return helper(i+1, prev)  # Can't take

    return helper(0)


@time_execution()
def sol_memo(nums: list[int]) -> int:
    memo = {}

    def helper(i: int, prev: int = float('-inf')) -> int:
        if i == len(nums):
            return 0
        key = (i, prev)
        if key in memo:
            return memo[key]

        # If we can take the current, split into two paths, where we take and where we don't take
        if nums[i] > prev:
            memo[key] = max(1+helper(i+1, nums[i]), helper(i+1, prev))
            return memo[key]

        memo[key] = helper(i+1, prev)  # Can't take
        return memo[key]

    return helper(0)


@time_execution()
def sol_v2(nums: list[int]) -> int:
    def helper(idx: int) -> int:
        maxlen = 0
        for i in range(idx+1, len(nums)):
            if nums[i] > nums[idx]:  # Num at idx is the last one we took
                maxlen = max(maxlen, helper(i))
        return 1 + maxlen

    return max(helper(idx) for idx in range(len(nums)))


@time_execution()
def sol_v2_memo(nums: list[int]) -> int:
    memo = {}

    def helper(idx: int) -> int:
        if idx in memo:
            return memo[idx]

        maxlen = 0
        for i in range(idx+1, len(nums)):
            if nums[i] > nums[idx]:  # Num at idx is the last one we took
                maxlen = max(maxlen, helper(i))

        memo[idx] = maxlen+1
        return memo[idx]

    return max(helper(idx) for idx in range(len(nums)))


@time_execution()
def sol_nx(nums: list[int]) -> int:
    G = nx.DiGraph()

    def helper(idx: int) -> None:
        if idx == len(nums):
            return

        for i in range(idx+1, len(nums)):
            if nums[i] > nums[idx]:
                G.add_edge(idx, i)
                helper(i)

    for i in range(len(nums)):
        helper(i)

    return 1+nx.dag_longest_path_length(G)


@time_execution()
def sol_bisect(nums: list[int]) -> int:
    stack = []
    for num in nums:
        idx = bisect.bisect_left(stack, num)
        if idx == len(stack):
            stack.append(num)
        else:
            stack[idx] = num

    return len(stack)
