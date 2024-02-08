if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an array of distinct integers 'candidates' and an integer 'target', 
    return a list of all unique combinations of candidates where the chosen numbers sum to target. 
    You may return the combinations in any order.
    The same number may be chosen from candidates an unlimited number of times. 
    Two combinations are unique if the frequency of at least one of the chosen numbers is different.'''


@time_execution()
def sol_dp(candidates: list[int], target: int) -> list[list[int]]:
    dp = [[] for _ in range(target+1)]
    dp[0] = [[]]
    for num in candidates:
        for i in range(num, target+1):
            for comb in dp[i-num]:
                dp[i].append(comb+[num])

    return dp[-1]


@time_execution()
def sol(candidates: list[int], target: int) -> list[int]:
    def helper(remainder: int, last_used_idx: int, combination: list[int]) -> None:
        if remainder == 0:
            combinations.append(combination)
            return

        for i in range(last_used_idx, len(candidates)):
            if (x := remainder-candidates[i]) >= 0:
                helper(x, i, combination+[candidates[i]])

    combinations = []
    helper(target, 0, [])
    return combinations


@time_execution()
def sol_v2(candidates: list[int], target: int) -> list[int]:
    def helper(remainder: int, last_used_idx: int, combination: list[int]) -> None:
        if last_used_idx == len(candidates):
            return
        if remainder == 0:
            combinations.append(combination)
            return

        if (x := remainder-candidates[last_used_idx]) >= 0:
            helper(x, last_used_idx, combination +
                   [candidates[last_used_idx]])  # Use the current number
        helper(remainder, last_used_idx+1, combination)  # Don't use it

    combinations = []
    helper(target, 0, [])
    return combinations


@time_execution()
def sol_v3(candidates: list[int], target: int) -> list[int]:
    def helper(remainder: int, last_used_idx: int) -> list[list[int]]:
        if remainder < 0 or last_used_idx == len(candidates):
            return []  # Falsy
        if remainder == 0:
            return [[]]  # Truthy

        combinations = []
        for i in range(last_used_idx, len(candidates)):
            # Returns a nested list
            for x in helper(remainder-candidates[i], i):
                combinations.append([candidates[i]]+x)

        return combinations

    return helper(target, 0)


@time_execution()
def sol_v3_memo(candidates: list[int], target: int) -> list[list[int]]:
    memo = {}

    def helper(remainder: int, last_used_idx: int) -> list[list[int]]:
        if remainder < 0 or last_used_idx == len(candidates):
            return []  # Falsy
        if remainder == 0:
            return [[]]  # Truthy

        key = (remainder, last_used_idx)
        if key in memo:
            return memo[key]

        combinations = []
        for i in range(last_used_idx, len(candidates)):
            # Returns a nested list
            for x in helper(remainder-candidates[i], i):
                combinations.append([candidates[i]]+x)

        memo[key] = combinations
        return combinations

    return helper(target, 0)


@time_execution()
def sol_backtrack(candidates: list[int], target: int) -> list[list[int]]:
    def helper(remainder: int, last_used_idx: int) -> None:
        if remainder == 0:
            combinations.append(combination.copy())
            return
        if remainder < 0:
            return

        for i in range(last_used_idx, len(candidates)):
            combination.append(candidates[i])
            helper(remainder-candidates[i], i)
            combination.pop()

    combination = []
    combinations = []
    helper(target, 0)
    return combinations
