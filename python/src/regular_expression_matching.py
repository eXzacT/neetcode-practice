if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an input string 's' and a pattern 'p', implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).'''


# @time_execution()
def sol_dp(s: str, p: str) -> bool:
    WIDTH = len(p) + 1
    HEIGHT = len(s) + 1
    dp = [[False] * WIDTH for _ in range(HEIGHT)]
    dp[0][0] = True  # Empty string matches empty pattern

    # For an empty string 's' the only way to match it with a non empty pattern is if after every character there's a star
    for j in range(1, WIDTH):
        if p[j-1] == '*':
            # p="a*" -> [0][1]=False(because a by itself) [0][2]=True(because * after a)
            dp[0][j] = dp[0][j-2]

    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            if p[j-1] == '*':
                # We could have possibly come here from same row, 2 cols to the left(Essentially ignoring the character before *)
                # OR from the previous row, meaning we matched whatever the character before * was
                dp[i][j] = dp[i][j - 2] or \
                    ((s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i-1][j])
            else:
                match = s[i - 1] == p[j - 1] or p[j - 1] == '.'
                # Current characters match and there was a match so far
                dp[i][j] = match and dp[i - 1][j - 1]

    return dp[-1][-1]


@time_execution()
def sol_dp_v2(s: str, p: str) -> bool:
    WIDTH = len(p) + 1
    HEIGHT = len(s) + 1
    prev = [False] * WIDTH
    prev[0] = True  # Empty string matches empty pattern

    # For an empty string 's' the only way to match it with a non empty pattern is if after every character there's a star
    for j in range(1, WIDTH):
        if p[j-1] == '*':
            # p="a*" -> [0][1]=False(because a by itself) [0][2]=True(because * after a)
            prev[j] = prev[j-2]

    for i in range(1, HEIGHT):
        curr = [False]*WIDTH
        for j in range(1, WIDTH):
            if p[j-1] == '*':
                # Zero occurrences of preceding character or one/more occurrences
                curr[j] = curr[j - 2] or \
                    ((s[i - 1] == p[j - 2] or p[j - 2] == '.') and prev[j])
            else:
                match = s[i - 1] == p[j - 1] or p[j - 1] == '.'
                # Current characters match and there was a match so far
                curr[j] = match and prev[j - 1]

        prev = curr

    return prev[-1]


@time_execution()
def sol_rec(s: str, p: str) -> bool:
    def helper(i: int, j: int) -> bool:
        if i == len(s) and j == len(p):  # Fully matched 's' string
            return True
        if j >= len(p):
            return False

        match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        if j+1 < len(p) and p[j+1] == '*':
            # Don't use the character before star, and use it if they actually match
            return helper(i, j+2) or match and helper(i+1, j)

        if match:
            return helper(i+1, j+1)

        return False

    return helper(0, 0)


@time_execution()
def sol_memo(s: str, p: str) -> bool:
    memo = {}

    def helper(i: int, j: int) -> bool:
        if i == len(s) and j == len(p):  # Fully matched 's' string
            return True
        if j >= len(p):
            return False
        key = (i, j)
        if key in memo:
            return memo[key]

        match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        if j+1 < len(p) and p[j+1] == '*':
            # Don't use the character before star or use it if the character before the star matches
            memo[key] = helper(i, j+2) or match and helper(i+1, j)
            return memo[key]

        if match:
            memo[key] = helper(i+1, j+1)
            return memo[key]

        memo[key] = False
        return False

    return helper(0, 0)


@time_execution()
def sol_memo_v2(s: str, p: str) -> bool:
    memo = [[None]*(len(p)+1) for _ in range(len(s)+1)]

    def helper(i: int, j: int) -> bool:
        if i == len(s) and j == len(p):  # Fully matched 's' string
            return True
        if j >= len(p):
            return False
        if memo[i][j] != None:
            return memo[i][j]

        match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        if j+1 < len(p) and p[j+1] == '*':
            # Don't use the character before star or use it if the character before the star matches
            memo[i][j] = helper(i, j+2) or match and helper(i+1, j)
            return memo[i][j]

        if match:
            memo[i][j] = helper(i+1, j+1)
            return memo[i][j]

        memo[i][j] = False
        return False

    return helper(0, 0)
