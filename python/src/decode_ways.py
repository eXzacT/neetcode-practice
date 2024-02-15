import networkx as nx
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' A message containing letters from A-Z can be encoded into numbers using the following mapping:
    'A' -> "1"
    'B' -> "2"
    ...
    'Z' -> "26"

    To decode an encoded message, all the digits must be grouped then mapped back into letters 
    using the reverse of the mapping above (there may be multiple ways). 
    For example, "11106" can be mapped into:

    "AAJF" with the grouping (1 1 10 6)
    "KJF" with the grouping (11 10 6)

    Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F'.
    Given a string 's' containing only digits, return the number of ways to decode it.'''


@time_execution()
def sol_dp(s: str) -> int:
    # Edge cases
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1

    dp = [0]*len(s)
    dp[0] = 1  # 1 Way to decode a single number
    # If the digit is 10 or 20 then it's still only 1 way to decode because later we would have a 0 by itself
    # If the digit is not 10 or 20 and it's between 10 and 26(incl) then we can have 2 ways to decode
    dp[1] = (1 <= int(s[0]+s[1]) <= 26) + (s[1] != '0')
    for i in range(2, len(s)):
        if s[i] != '0':
            dp[i] += dp[i-1]
        if 10 <= int(s[i-1]+s[i]) <= 26:
            dp[i] += dp[i-2]

    return dp[-1]


@time_execution()
def sol_dp_v2(s: str) -> int:
    # Edge cases
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1

    prevprev = 1
    prev = (1 <= int(s[0]+s[1]) <= 26) + (s[1] != '0')
    for i in range(2, len(s)):
        temp = 0
        if s[i] != '0':
            temp += prev
        if 10 <= int(s[i-1]+s[i]) <= 26:
            temp += prevprev
        prevprev, prev = prev, temp

    return prev


@time_execution()
def sol(s: str) -> int:
    if s[0] == "0":
        return 0

    def helper(i: int) -> int:
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0

        # We can either take 1 or 2 digits
        if i+1 < len(s) and 10 <= int(s[i]+s[i+1]) <= 26:
            return helper(i+1)+helper(i+2)

        return helper(i+1)  # Can only take 1 digit

    return helper(0)


@time_execution()
def sol_memo(s: str) -> int:
    if s[0] == "0":
        return 0

    memo = {len(s): 1}

    def helper(i: int) -> int:
        if i in memo:
            return memo[i]
        if s[i] == "0":
            return 0

        # We can either take 1 or 2 digits
        if i+1 < len(s) and 10 <= int(s[i]+s[i+1]) <= 26:
            memo[i] = helper(i+1)+helper(i+2)
            return memo[i]

        memo[i] = helper(i+1)  # Can only take 1 digit
        return memo[i]

    return helper(0)


@time_execution()
def sol_v2(s: str) -> int:
    def helper(i: int) -> int:
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0

        if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
            return helper(i+1)+helper(i+2)
        return helper(i+1)

    return helper(0)


@time_execution()
def sol_v2_memo(s: str) -> int:
    memo = {len(s): 1}

    def helper(i: int) -> int:
        if i in memo:
            return memo[i]
        if s[i] == "0":
            return 0

        if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
            memo[i] = helper(i+1)+helper(i+2)
            return memo[i]

        memo[i] = helper(i+1)
        return memo[i]

    return helper(0)


@time_execution()
def sol_nx(s: str) -> int:
    if s[0] == "0":
        return 0

    def helper(i: int) -> None:
        if i < len(s) and s[i] == '0':
            return
        if i >= len(s)-1:
            G.add_edge(i, len(s))
            return

        if 10 <= int(s[i]+s[i+1]) <= 26:
            G.add_edge(i, i+1)
            helper(i+1)
            G.add_edge(i, i+2)
            helper(i+2)
        else:
            G.add_edge(i, i+1)
            helper(i+1)

    G = nx.DiGraph()
    helper(0)

    return len(list(nx.all_simple_paths(G, source=0, target=len(s)))) if G.has_node(len(s)) else 0
