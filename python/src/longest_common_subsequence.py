from collections import defaultdict
import bisect
import networkx as nx
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given two strings text1 and text2, return the length of their longest common subsequence. 
    If there is no common subsequence, return 0.
    A subsequence of a string is a new string generated using some characters from the original string in the same order they were in.
    For example, "ace" is a subsequence of "abcde".
    A common subsequence of two strings is a subsequence that is common to both strings.'''


@time_execution()
def sol_dp(text1: str, text2: str) -> int:
    WIDTH = len(text2)+1
    HEIGHT = len(text1)+1
    dp = [[0]*WIDTH for _ in range(HEIGHT)]
    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


@time_execution()
def sol_dp_v2(text1: str, text2: str) -> int:
    WIDTH = len(text2)+1
    HEIGHT = len(text1)+1

    prev = [0]*WIDTH

    for i in range(1, HEIGHT):
        left = 0
        for j in range(1, WIDTH):
            if text1[i-1] == text2[j-1]:
                prev[j] = 1+left
            else:
                prev[j] = max(prev[j], left)

            left = prev[j]

    return prev[-1]


@time_execution()
def sol_rec(text1: str, text2: str) -> int:
    def helper(i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            return 1+helper(i+1, j+1)
        return max(helper(i+1, j), helper(i, j+1))

    return helper(0, 0)


@time_execution()
def sol_memo(text1: str, text2: str) -> int:
    memo = {}

    def helper(i: int, j: int) -> int:
        if i == len(text1) or j == len(text2):
            return 0
        key = (i, j)
        if key in memo:
            return memo[key]

        if text1[i] == text2[j]:
            return 1+helper(i+1, j+1)

        memo[key] = max(helper(i+1, j), helper(i, j+1))
        return memo[key]

    return helper(0, 0)


@time_execution()
def sol_nx(text1: str, text2: str) -> int:
    G = nx.DiGraph()
    stack = [(0, 0)]
    visited = set()

    while stack:
        i, j = stack.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))

        if i == len(text1) or j == len(text2):
            continue
        if text1[i] == text2[j]:
            G.add_edge((i, j), (i+1, j+1), weight=1)
            stack.append((i+1, j+1))
            continue
        else:
            G.add_edge((i, j), (i+1, j), weight=0)
            stack.append((i+1, j))
            G.add_edge((i, j), (i, j+1), weight=0)
            stack.append((i, j+1))

    return nx.dag_longest_path_length(G)


@time_execution()
def sol_hunt_szymanski(a: str, b: str) -> int:
    a_indices = defaultdict(list)

    # Create a dictionary of chars and their positions, list because a same character can have multiple positions
    for idx, char in enumerate(a):
        a_indices[char].append(idx)

    # Then reverse those positions for each char
    for indices in a_indices.values():
        indices.reverse()

    # List of characters positions in string a that are also in string b, in the order they show up in string b
    # So if we had a="abcae" and b="ace" filtered will be [3,0,2,4], 3,0 comes from letter "a", we reversed the list previously
    a_filtered = []
    for char in b:
        a_filtered.extend(a_indices[char])

    lcs = []
    for ai in a_filtered:
        # Find the position to insert the current index in the LCS list to keep it sorted
        pos = bisect.bisect_left(lcs, ai)
        # If the position is at the end of the LCS list, we can just append it
        # Otherwise, replace the element at found position with current index
        if pos == len(lcs):
            lcs.append(ai)
        else:
            lcs[pos] = ai

    return len(lcs)
