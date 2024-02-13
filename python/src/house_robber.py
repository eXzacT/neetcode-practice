import networkx as nx

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an integer array nums representing the amount of money of each house
    Once you rob a house you are not allowed to rob its neighbour.
    Return the maximum amount of money you can rob without alerting the police.'''


@time_execution()
def sol_dp(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(nums[i]+dp[i-2], dp[i-1])

    return dp[-1]


@time_execution(executions=1000)
def sol_dp_v2(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    prevprev = nums[0]
    prev = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        prevprev, prev = prev, max(prevprev+nums[i], prev)

    return prev


@time_execution(executions=1000)
def sol_dp_v3(nums: list[int]) -> int:
    prevprev, prev = 0, 0

    for num in nums:
        prevprev, prev = prev, max(prevprev+num, prev)

    return prev


@time_execution()
def sol_taiL_rec(nums: list[int]) -> int:
    def helper(i: int, prevprev: int = 0, prev: int = 0):
        if i == len(nums):
            return prev

        return helper(i+1, prev, max(nums[i]+prevprev, prev))

    return helper(0)


@time_execution()
def sol_rec(nums: list[int]) -> int:
    def helper(i: int):
        if i >= len(nums):
            return 0

        # Rob and move on 2 houses vs not rob and move on by 1
        return max(nums[i]+helper(i+2), helper(i+1))

    return helper(0)


@time_execution()
def sol_memo(nums: list[int]) -> int:
    memo = {}

    def helper(i: int) -> int:
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]

        # Rob and move on 2 houses vs not rob and move on by 1
        memo[i] = max(nums[i]+helper(i+2), helper(i+1))
        return memo[i]

    return helper(0)


@time_execution()
def sol_nx(nums: list[int]) -> int:
    G = nx.DiGraph()

    # Add a dummy source and sink to simplify edge cases
    source, sink = -1, len(nums)
    G.add_node(source)
    G.add_node(sink)

    # Connect the source to the first two houses as potential starting points
    if nums:
        G.add_edge(source, 0, weight=nums[0])
    if len(nums) > 1:
        G.add_edge(source, 1, weight=nums[1])

    # Add edges for the rest of the houses
    for i in range(len(nums)):
        # Skip robbing
        if i + 1 < len(nums):
            G.add_edge(i, i + 1, weight=0)
        # Rob
        if i + 2 < len(nums):
            G.add_edge(i, i + 2, weight=nums[i + 2])
        # Connect last two houses to the sink with 0 weight
        if i == len(nums) - 1 or i == len(nums) - 2:
            G.add_edge(i, sink, weight=0)

    return nx.dag_longest_path_length(G)
