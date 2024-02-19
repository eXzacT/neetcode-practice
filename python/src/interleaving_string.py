if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
    An interleaving of two strings s and t is a configuration where we split those two strings into substrings
    and use those substrings in the order they were split in. So after using a substring of s we have to use a substr of t next'''


@time_execution()
def sol_dp(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1)+len(s2):
        return False

    HEIGHT = len(s1)+1
    WIDTH = len(s2)+1
    dp = [[False]*WIDTH for _ in range(HEIGHT)]
    dp[0][0] = True  # Empty strings are true

    # How far can we get using just the starting substring from either words
    i = 1
    while i < HEIGHT and dp[i-1][0]:
        dp[i][0] = s1[i-1] == s3[i-1]
        i += 1
    j = 1
    while j < WIDTH and dp[0][j-1]:
        dp[0][j] = s2[j-1] == s3[j-1]
        j += 1

    # We can reach any other position if the position left or above was True AND we can match the current character
    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]
                        ) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

    return dp[-1][-1]


@time_execution()
def sol_dp_v2(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1) + len(s2):
        return False

    HEIGHT = len(s1) + 1
    WIDTH = len(s2) + 1
    prev = [False] * WIDTH
    prev[0] = True  # Empty strings are true

    j = 1  # For as long as we can create the beginning of s3 using the starting substring of s2
    while j < WIDTH and s2[j-1] == s3[j-1]:
        prev[j] = True
        j += 1

    for i in range(1, HEIGHT):
        # Could we have gotten to this row(first column) using just the first word?
        prev[0] = prev[0] and s1[i-1] == s3[i-1]
        # We can reach any other position in 2 cases
        # 1. If we came from above and we're now matching s1(HEIGHT)(meaning going down)
        # 2. If we came from left and we're now matching s2(WIDTH)(meaning going right)
        for j in range(1, WIDTH):
            prev[j] = (prev[j] and s1[i-1] == s3[i+j-1]
                       ) or (prev[j-1] and s2[j-1] == s3[i+j-1])

    return prev[-1]


@time_execution()
def sol_rec(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1)+len(s2):
        return False

    def helper(i: int, j: int, string_so_far: str = "") -> bool:
        if i == len(s1):
            return string_so_far+s2[j:] == s3
        if j == len(s2):
            return string_so_far+s1[i:] == s3

        if s3.startswith(string_so_far):
            return helper(i+1, j, string_so_far+s1[i]) or helper(i, j+1, string_so_far+s2[j])

        return False

    return helper(0, 0)


@time_execution()
def sol_memo(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1)+len(s2):
        return False

    memo = {}

    def helper(i: int, j: int, string_so_far: str = "") -> bool:
        key = (i, j)
        if key in memo:
            return memo[key]
        if i == len(s1):
            return string_so_far+s2[j:] == s3
        if j == len(s2):
            return string_so_far+s1[i:] == s3

        if s3.startswith(string_so_far):
            memo[key] = helper(i+1, j, string_so_far+s1[i]
                               ) or helper(i, j+1, string_so_far+s2[j])
            return memo[key]

        memo[key] = False
        return False

    return helper(0, 0)


@time_execution()
def sol_rec_v2(s1: str, s2: str, s3: str) -> bool:
    if len(s3) < len(s1)+len(s2):
        return False

    def helper(i: int, j: int) -> bool:
        # If we reached end of any string then check the rest of other string
        if i == len(s1):
            return s3[i+j:] == s2[j:]
        if j == len(s2):
            return s3[i+j:] == s1[i:]

        # Can we interleave if we start taking from s1?
        if s3[i+j] == s1[i] and helper(i+1, j):
            return True
        # Can we interleave if we start taking from s2?
        if s3[i+j] == s2[j] and helper(i, j+1):
            return True

        return False

    return helper(0, 0)


@time_execution()
def sol_memo_v2(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1)+len(s2):
        return False
    memo = {}

    def helper(i: int, j: int) -> bool:
        key = (i, j)
        if key in memo:
            return memo[key]
        # If we reached end of any string then check the rest of other string
        if i == len(s1):
            return s3[i+j:] == s2[j:]
        if j == len(s2):
            return s3[i+j:] == s1[i:]

        if s3[i+j] == s1[i] and helper(i+1, j):
            memo[key] = True
            return True
        if s3[i+j] == s2[j] and helper(i, j+1):
            memo[key] = True
            return True

        memo[key] = False
        return False

    return helper(0, 0)
