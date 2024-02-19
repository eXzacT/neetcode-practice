import networkx as nx
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
    You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character
    
    This is also known as Levenshtein distance.'''


@time_execution()
def sol_dp(word1: str, word2: str) -> int:
    WIDTH = len(word2)+1
    HEIGHT = len(word1)+1
    dp = [[0]*WIDTH for _ in range(HEIGHT)]

    # If one word is an empty string, then the edit distance is equal to the non empty string length
    for j in range(1, WIDTH):
        dp[0][j] = j
    for i in range(1, HEIGHT):
        dp[i][0] = i

    for i in range(1, HEIGHT):
        for j in range(1, WIDTH):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[-1][-1]


@time_execution()
def sol_dp_v2(word1: str, word2: str) -> int:
    WIDTH = len(word2)+1
    HEIGHT = len(word1)+1

    # If one word is an empty string, then the edit distance is equal to the non empty string length
    prev = [j for j in range(WIDTH)]

    for i in range(1, HEIGHT):
        curr = [i]+[0]*(WIDTH-1)  # Leftmost starts as index of the row
        for j in range(1, WIDTH):
            if word1[i-1] == word2[j-1]:
                curr[j] = prev[j-1]
            else:
                curr[j] = 1+min(prev[j], curr[j-1], prev[j-1])

        prev = curr

    return prev[-1]


@time_execution()
def sol_rec(word1: str, word2: str) -> int:
    def helper(i: int, j: int) -> int:
        if i == len(word1) or j == len(word2):
            return len(word1)-i+len(word2)-j

        if word1[i] == word2[j]:
            return helper(i+1, j+1)
        # Moving i by 1 simulates deletion, moving j by 1 simulates insertion, moving both by 1 simulates replacement
        return 1+min(helper(i+1, j), helper(i, j+1), helper(i+1, j+1))

    return helper(0, 0)


@time_execution()
def sol_memo(word1: str, word2: str) -> int:
    memo = {}

    def helper(i: int, j: int) -> int:
        if i == len(word1) or j == len(word2):
            return len(word1)-i+len(word2)-j
        key = (i, j)
        if key in memo:
            return memo[key]

        if word1[i] == word2[j]:
            memo[key] = helper(i+1, j+1)
            return memo[key]

        # Moving i by 1 simulates deletion, moving j by 1 simulates insertion, moving both by 1 simulates replacement
        memo[key] = 1+min(helper(i+1, j), helper(i, j+1), helper(i+1, j+1))
        return memo[key]

    return helper(0, 0)


@time_execution()
def sol_nx(word1: str, word2: str) -> int:
    G = nx.DiGraph()
    stack = [(0, 0)]
    visited = set()
    dummy_node = (-1, -1)

    while stack:
        i, j = stack.pop()
        if (i, j) in visited:
            continue
        visited.add((i, j))

        if i == len(word1) or j == len(word2):
            G.add_edge((i, j), dummy_node, weight=len(word1)-i + len(word2)-j)
            continue
        if word1[i] == word2[j]:
            G.add_edge((i, j), (i+1, j+1), weight=0)
            stack.append((i+1, j+1))
            continue

        G.add_edge((i, j), (i+1, j), weight=1)
        stack.append((i+1, j))
        G.add_edge((i, j), (i, j+1), weight=1)
        stack.append((i, j+1))
        G.add_edge((i, j), (i+1, j+1), weight=1)
        stack.append((i+1, j+1))

    return nx.shortest_path_length(G, source=(0, 0), target=dummy_node, weight="weight")
