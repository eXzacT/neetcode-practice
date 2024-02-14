import networkx as nx
import heapq
from collections import deque

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an integer array nums, return true if you can partition the array into two subsets 
    such that the sum of the elements in both subsets is equal or false otherwise.'''


@time_execution()
def sol_dp(nums: list[int]) -> bool:
    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    dp = [False]*(half_sum+1)
    dp[0] = True  # Sum up to 0 by not taking anything

    for num in nums:
        # By going in reverse we make sure not to reuse current number more than once
        # Meaning we didn't change dp of some index to True during current loop
        for curr_sum in range(half_sum, num-1, -1):
            if dp[curr_sum-num]:
                dp[curr_sum] = True
                if curr_sum == half_sum:  # Early return
                    return True

    return False


@time_execution()
def sol_dp_v2(nums: list[int]) -> bool:
    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    sums = {0}

    for num in nums:
        new_sums = set()
        for curr_sum in sums:
            new_sum = curr_sum + num
            if new_sum == half_sum:
                return True
            if new_sum < half_sum:
                new_sums.add(new_sum)

        sums.update(new_sums)

    return False


@time_execution()
def sol(nums: list[int]) -> bool:
    def helper(sum1: int, sum2: int, idx: int) -> bool:
        if idx == len(nums):
            return sum1 == sum2

        # Path where we add current number to sum1 and where we add it to sum2
        return helper(sum1+nums[idx], sum2, idx+1) or helper(sum1, sum2+nums[idx], idx+1)

    if sum(nums) % 2 != 0:
        return False
    return helper(0, 0, 0)


@time_execution()
def sol_memo(nums: list[int]) -> bool:
    memo = {}

    def helper(sum1: int, sum2: int, idx: int) -> bool:
        if idx == len(nums):
            return sum1 == sum2
        key = (idx, sum1, sum2)
        if key in memo:
            return memo[key]

        # Path where we add current number to sum1 and where we add it to sum2
        memo[key] = helper(sum1+nums[idx], sum2, idx +
                           1) or helper(sum1, sum2+nums[idx], idx+1)
        return memo[key]

    if sum(nums) % 2 != 0:
        return False
    return helper(0, 0, 0)


@time_execution()
def sol_v2(nums: list[int]) -> bool:
    def helper(idx: int, remainder: int) -> bool:
        if idx == len(nums):
            return False
        if remainder == 0:
            return True

        for i in range(idx, len(nums)):
            if (x := remainder-nums[i]) >= 0:
                if helper(i+1, x):
                    return True

        return False

    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    return helper(0, half_sum)


@time_execution()
def sol_v2_memo(nums: list[int]) -> bool:
    memo = {}

    def helper(idx: int, remainder: int) -> bool:
        if idx == len(nums):
            return False
        if remainder == 0:
            return True
        key = (idx, remainder)
        if key in memo:
            return memo[key]

        for i in range(idx, len(nums)):
            if (x := remainder-nums[i]) >= 0:
                if helper(i+1, x):
                    return True

        memo[key] = False
        return memo[key]

    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    return helper(0, half_sum)


@time_execution()
def sol_v3(nums: list[int]) -> bool:
    def helper(idx: int, remainder: int) -> bool:
        if idx == len(nums):
            return False
        if remainder == 0:
            return True

        return helper(idx+1, remainder-nums[idx]) or helper(idx+1, remainder)

    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False
    return helper(0, half_sum)


@time_execution()
def sol_v3_memo(nums: list[int]) -> bool:
    memo = {}

    def helper(idx: int, remainder: int) -> bool:
        if idx == len(nums):
            return False
        if remainder == 0:
            return True

        key = (remainder, idx)
        if key in memo:
            return memo[key]

        memo[key] = helper(idx+1, remainder-nums[idx]
                           ) or helper(idx+1, remainder)
        return memo[key]

    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False
    return helper(0, half_sum)


@time_execution()
def sol_pq(nums: list[int]) -> bool:
    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    pq = []
    heapq.heappush(pq, (0, 0))
    while pq:
        sum_so_far, idx = heapq.heappop(pq)
        for i in range(idx, len(nums)):
            new_sum = sum_so_far-nums[i]
            if new_sum == -half_sum:
                return True
            if new_sum > -half_sum:
                heapq.heappush(pq, (new_sum, i+1))

    return False


@time_execution()
def sol_bfs(nums: list[int]) -> bool:
    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    queue = deque([(0, half_sum)])
    while queue:
        idx, remainder = queue.popleft()

        for i in range(idx, len(nums)):
            new_sum = remainder-nums[i]
            if new_sum == 0:
                return True
            if new_sum >= 0:
                queue.append((i+1, new_sum))

    return False


@time_execution()
def sol_nx(nums: list[int]) -> bool:
    half_sum, remainder = divmod(sum(nums), 2)
    if remainder:
        return False

    G = nx.DiGraph()

    def helper(idx: int, remainder: int) -> None:
        # No reason to keep adding nodes
        if remainder <= 0 or idx == len(nums):
            return

        for i in range(idx, len(nums)):
            G.add_edge(remainder, remainder-nums[i])
            helper(i+1, remainder-nums[i])

    helper(0, half_sum)
    return G.has_node(0)
