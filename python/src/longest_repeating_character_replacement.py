from collections import Counter

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase 
    English character. You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter you can get after performing the above operations.'''


@time_execution()
def sol(s: str, k: int) -> int:
    l = 0
    count = {}

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        # If we have to replace more characters than is allowed, shrink from the left
        if (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

    # Largest window size
    return r - l + 1


@time_execution()
def sol_optimized(s: str, k: int) -> int:
    most_common = l = 0
    count = {}

    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        most_common = max(most_common, count[s[r]])

        # If we have to replace more characters than is allowed, shrink from the left
        if (r - l + 1) - most_common > k:
            count[s[l]] -= 1
            l += 1

    # Largest window size
    return r - l + 1
