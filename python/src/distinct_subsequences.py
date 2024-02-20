if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given two strings 's' and 't', return the number of distinct subsequences of 's' which equals 't'.'''


@time_execution()
def sol_dp(s: str, t: str) -> int:
    WIDTH = len(t)+1
    HEIGHT = len(s)+1

    # First col in every row is 1, meaning for any length 's' we can create an empty string 't' with 1 unique way, by not using any letters
    dp = [[1]+[0]*(WIDTH-1) for _ in range(HEIGHT)]

    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


@time_execution()
def sol_dp_v2(s: str, t: str) -> int:
    WIDTH = len(t)+1
    HEIGHT = len(s)+1

    # 1 way to create an empty string "t" from any length string "s"
    prev = [0]*WIDTH
    prev[0] = 1

    for i in range(1, HEIGHT):
        temp = prev[:]
        for j in range(1, WIDTH):
            if s[i-1] == t[j-1]:
                prev[j] = temp[j-1]+temp[j]

    return prev[-1]


@time_execution()
def sol_rec(s: str, t: str) -> int:
    def helper(i: int, j: int, string_so_far: str = "") -> int:
        if i == len(s) or j == len(t):
            return 1 if string_so_far == t else 0

        if s[i] == t[j]:  # Use the character or look for the next one that matches
            return helper(i+1, j+1, string_so_far+s[i])+helper(i+1, j, string_so_far)
        return helper(i+1, j, string_so_far)

    return helper(0, 0)


@time_execution()
def sol_memo(s: str, t: str) -> int:
    memo = {}

    def helper(i: int, j: int, string_so_far: str = "") -> int:
        key = (i, j)
        if key in memo:
            return memo[key]

        if i == len(s) or j == len(t):
            memo[key] = 1 if string_so_far == t else 0
            return memo[key]

        if s[i] == t[j]:  # Use the character or look for the next one that matches
            memo[key] = helper(i+1, j+1, string_so_far+s[i]) + \
                helper(i+1, j, string_so_far)
            return memo[key]

        memo[key] = helper(i+1, j, string_so_far)
        return memo[key]

    return helper(0, 0)


@time_execution()
def sol_rec_v2(s: str, t: str) -> int:
    def helper(i: int, j: int) -> int:
        if j == len(t):  # Managed to create the entire word 't' using letters from 's'
            return 1
        if i == len(s):
            return 0

        if s[i] == t[j]:  # Use the character or look for the next one that matches
            return helper(i+1, j+1)+helper(i+1, j)
        return helper(i+1, j)

    return helper(0, 0)


@time_execution()
def sol_memo_v2(s: str, t: str) -> int:
    memo = {}

    def helper(i: int, j: int) -> int:
        if j == len(t):  # Managed to create the entire word 't' using letters from 's'
            return 1
        if i == len(s):
            return 0

        key = (i, j)
        if key in memo:
            return memo[key]

        if s[i] == t[j]:  # Use the character or look for the next one that matches
            memo[key] = helper(i+1, j+1)+helper(i+1, j)
            return memo[key]

        return helper(i+1, j)

    return helper(0, 0)
