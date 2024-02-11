if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given a collection of integer 'candidates' and an integer 'target', find all unique combinations in candidates where the candidate numbers sum to target.
    Each number in candidates may only be used once in the combination.
    Note: The solution set must not contain duplicate combinations.'''


@time_execution()
def sol_naive(candidates: list[int], target: int) -> list[list[int]]:
    combinations = set()
    candidates = sorted(candidates)

    def helper(remainder: int, i: int, combination: list[int] = []) -> None:
        if remainder == 0:
            combinations.add(tuple(combination))
            return
        if i == len(candidates) or candidates[i] > remainder or remainder < 0:
            return

        helper(remainder-candidates[i], i+1, combination+[candidates[i]])

        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1

        helper(remainder, i+1, combination)

    helper(target, 0)
    return [list(c) for c in combinations]


@time_execution()
def sol_optimized(candidates: list[int], target: int) -> list[list[int]]:
    combinations = []
    candidates = sorted(candidates)

    def helper(remainder: int, i: int, combination: list[int] = []) -> None:
        if remainder == 0:
            combinations.append(combination)
            return
        if i == len(candidates) or candidates[i] > remainder or remainder < 0:
            return

        helper(remainder-candidates[i], i+1, combination+[candidates[i]])

        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1

        helper(remainder, i+1, combination)

    helper(target, 0)
    return combinations


@time_execution()
def sol_optimized_v2(candidates: list[int], target: int) -> list[list[int]]:
    combinations = []
    candidates = sorted(candidates)

    def helper(remainder: int, i: int, combination: list[int]) -> None:
        if remainder == 0:
            combinations.append(combination[:])
            return
        if i == len(candidates) or candidates[i] > remainder or remainder < 0:
            return

        combination.append(candidates[i])
        helper(remainder-candidates[i], i+1, combination)

        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1

        combination.pop()
        helper(remainder, i+1, combination)

    helper(target, 0, [])
    return combinations


@time_execution()
def sol_optimized_v3(candidates: list[int], target: int) -> list[list[int]]:
    combinations = []
    combination = []
    candidates = sorted(candidates)

    def helper(remainder: int, i: int) -> None:
        if remainder == 0:
            combinations.append(combination[:])
            return
        if i == len(candidates) or candidates[i] > remainder or remainder < 0:
            return

        combination.append(candidates[i])
        helper(remainder-candidates[i], i+1)

        while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
            i += 1

        combination.pop()
        helper(remainder, i+1)

    helper(target, 0)
    return combinations


@time_execution()
def sol_optimized_v4(candidates: list[int], target: int) -> list[list[int]]:
    candidates = sorted(candidates)
    combinations = []

    def helper(remainder: int, idx: int, combination: list[int]) -> None:
        if remainder == 0:
            combinations.append(combination[:])
            return
        if remainder < 0:
            return

        prev = -1
        for i in range(idx, len(candidates)):
            if candidates[i] > remainder:
                break
            if prev == candidates[i]:
                continue
            combination.append(candidates[i])
            helper(remainder - candidates[i], i+1, combination)
            combination.pop()
            prev = candidates[i]

    helper(target, 0, [])
    return combinations
