if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given a string 's', partition 's' in such a way so every substring is a palindrome
    Return all possible palindrome partitioning of s.'''


@time_execution()
def sol_naive(s: str) -> list[list[str]]:
    def helper(i: int) -> list[list[str]]:
        if i == len(s):
            substrs.append(substr[:])
            return

        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                substr.append(s[i:j])
                helper(j)
                substr.pop()

    substr = []
    substrs = []
    helper(0)
    return substrs


@time_execution()
def sol_better(s: str) -> list[list[str]]:
    def is_palindrome(l: int, r: int) -> bool:
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    def helper(i: int) -> list[list[str]]:
        if i == len(s):
            substrs.append(substr[:])
            return

        # Start from i+1 to skip an empty string, go to len+1 because [:upper] is non inclusive
        for j in range(i+1, len(s)+1):
            # -1 because we're checking the actual character at that index
            if is_palindrome(i, j-1):
                substr.append(s[i:j])
                helper(j)
                substr.pop()

    substr = []
    substrs = []
    helper(0)
    return substrs
