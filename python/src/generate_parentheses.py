if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.'''


@time_execution()
def sol_rec(n: int) -> list[str]:
    def helper(open_count: int, comb: str) -> None:
        # If at any point we have more closed parentheses than open then it's invalid
        if len(comb) - open_count > open_count:
            return
        # Reached the full combination
        if len(comb) == n*2:
            combinations.append(comb)
            return
        # We can only close since we have 3 open parentheses
        if open_count == n:
            helper(open_count, comb+')')
            return

        helper(open_count+1, comb+'(')
        helper(open_count, comb+')')

    combinations = []
    helper(1, '(')
    return combinations


@time_execution()
def sol_backtrack(n: int) -> list[str]:
    def helper(open_count: int, close_count: int):
        # Combination is of the required length
        if len(combination) == 2 * n:
            combinations.append(''.join(combination))
            return

        # If we can add an opening parenthesis, add and explore further
        if open_count < n:
            combination.append('(')
            helper(open_count + 1, close_count)
            combination.pop()

        # If we can add a closing parenthesis, add and explore further
        if close_count < open_count:
            combination.append(')')
            helper(open_count, close_count + 1)
            combination.pop()

    combinations = []
    combination = []
    helper(0, 0)
    return combinations


@time_execution()
def sol_backtrack_v2(n: int) -> list[str]:
    def helper(open_count: int):
        # Combination is of the required length
        if len(combination) == 2 * n:
            combinations.append(''.join(combination))
            return

        # Allowed to add an opening parentheses
        if open_count < n:
            combination.append('(')
            helper(open_count + 1)
            combination.pop()

        # Less closed than open, which means we can add a close parentheses
        if len(combination)-open_count < open_count:
            combination.append(')')
            helper(open_count)
            combination.pop()

    combination = []
    combinations = []
    helper(0)
    return combinations


@time_execution()
def sol_iter(n: int) -> list[str]:
    stack = [(1, '(')]
    combinations = []
    while stack:
        open_count, comb = stack.pop()
        if len(comb) == n*2:
            combinations.append(comb)
            continue

        if len(comb)-open_count < open_count:
            stack.append((open_count, comb+')'))
        if open_count < n:
            stack.append((open_count+1, comb+'('))

    return combinations
