import matplotlib.pyplot as plt
import networkx as nx
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an integer array 'nums' representing the amount of money each house has.
    Unlike house robber I in this problem houses are in a circular street.
    You are only allowed to rob non adjacent houses. So if you chose first you can't pick its adjacent neighbours, 2nd and last.
    Return the maximum amount of money you can rob tonight without alerting the police.'''


@time_execution()
def sol_dp(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    # Include first element
    incl = [0] * (len(nums)-1)
    incl[0] = nums[0]
    incl[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)-1):  # Don't include last
        incl[i] = max(
            incl[i-1], nums[i] + incl[i-2])

    # Exclude first element
    excl = [0] * (len(nums)-1)
    excl[0] = nums[1]
    excl[1] = max(nums[1], nums[2])
    for i in range(3, len(nums)):  # Include last
        # Everything off by 1 except nums, because we skipped the first number
        excl[i-1] = max(
            excl[i-2], nums[i] + excl[i-3])

    return max(excl[-1], incl[-1])


@time_execution()
def sol_dp_v2(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    # Exclude last, include first
    prevprev, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)-1):
        prevprev, prev1 = prev1, max(
            prevprev+nums[i], prev1)

    # Include last, exclude first
    prevprev2, prev2 = nums[1], max(nums[1], nums[2])
    for i in range(3, len(nums)):
        prevprev2, prev2 = prev2, max(
            prevprev2+nums[i], prev2)

    return max(prev1, prev2)


@time_execution()
def sol_taiL_rec(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    def helper(i: int, incl: bool, prevprev: int = 0, prev: int = 0):
        if incl:
            if i == len(nums)-1:
                return prev
        else:
            if i == len(nums):
                return prev

        return helper(i+1, incl, prev, max(nums[i]+prevprev, prev))

    return max(helper(0, True), helper(1, False))


@time_execution()
def sol_rec(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def helper(i: int, odd: bool) -> int:
        if i == len(nums):
            return 0
        if i == len(nums)-1:
            if odd:  # We started from first so can't use the last since they're adjacent
                return -nums[0]+max(nums[0], nums[-1])
            else:  # Didn't start from first, okay to use last
                return nums[i]

        return max(nums[i]+helper(i+2, odd), helper(i+1, odd))

    return max(nums[0]+helper(2, True), helper(1, False))


@time_execution()
def sol_memo(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    memo = {}

    def helper(i: int, odd: bool) -> int:
        key = (i, odd)
        if key in memo:
            return memo[key]
        if i == len(nums):
            return 0
        if i == len(nums)-1:
            if odd:  # We started from first so can't use the last since they're adjacent
                return -nums[0]+max(nums[0], nums[-1])
            else:  # Didn't start from first, okay to use last
                return nums[i]

        memo[key] = max(nums[i]+helper(i+2, odd), helper(i+1, odd))
        return memo[key]

    return max(helper(1, False), nums[0]+helper(2, True))


@time_execution()
def sol_nx(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    G1 = nx.DiGraph()
    # Populate graph where we take exclude the first one and can take last one
    G1.add_edge(0, 1, weight=0)
    for i in range(1, len(nums)):
        G1.add_edge(i, i+1, weight=0)
        G1.add_edge(i, i+2, weight=nums[i])

    G2 = nx.DiGraph()
    # Populate graph where we include the first one and can't take the last one
    G2.add_edge(0, 2, weight=nums[0])
    for i in range(2, len(nums)-1):
        G2.add_edge(i, i+1, weight=0)
        G2.add_edge(i, i+2, weight=nums[i])

    return max(nx.dag_longest_path_length(G1), nx.dag_longest_path_length(G2))
