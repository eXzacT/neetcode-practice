if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an m x n 'board' of characters and a list of strings 'words', return all words on the board.

    Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
    The same letter cell may not be used more than once in a word.'''


@time_execution()
def sol_naive(board: list[list[str]], words: list[str]) -> list[str]:
    WIDTH = len(board[0])
    HEIGHT = len(board)

    def dfs(i: int, j: int, k: int, word: str, visited: set) -> bool:
        if word[k] != board[i][j]:
            return False
        if k == len(word)-1:
            return word[k] == board[i][j]

        if word[k] == board[i][j]:
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and (ni, nj) not in visited:
                    if dfs(ni, nj, k+1, word, visited | {(ni, nj)}):
                        return True

        return False

    res = []
    for word in words:
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if dfs(i, j, 0, word, set([(i, j)])):
                    res.append(word)
                    break

            else:  # Didn't break
                continue
            break  # If we broke break again

    return res


class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word: str) -> None:
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()

            curr = curr.children[c]

        curr.is_word = True


@time_execution()
def sol_trie_node(board: list[list[str]], words: list[str]) -> list[str]:
    WIDTH = len(board[0])
    HEIGHT = len(board)

    root = Node()
    for word in words:
        root.add_word(word)

    res, visited = set(), set()

    def dfs(i: int, j: int, curr: Node, word: str) -> None:
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and board[ni][nj] in curr.children and (ni, nj) not in visited:
                visited.add((ni, nj))

                dfs(ni, nj, curr.children[board[ni][nj]], word+board[ni][nj])

                visited.remove((ni, nj))

        if curr.is_word:
            res.add(word)

        return False

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] in root.children:  # We can start forming the word
                visited.add((i, j))
                dfs(i, j, root.children[board[i][j]], board[i][j])
                visited.remove((i, j))

    return list(res)


@time_execution()
def sol_trie(board: list[list[str]], words: list[str]) -> list[str]:
    WIDTH = len(board[0])
    HEIGHT = len(board)
    trie: dict[str, dict] = {}

    for word in words:
        curr = trie
        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]

        curr["$"] = {}

    res, visited = set(), set()

    def dfs(i: int, j: int, curr: dict[str, dict], word: str) -> None:
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and board[ni][nj] in curr and (ni, nj) not in visited:
                visited.add((ni, nj))

                dfs(ni, nj, curr[board[ni][nj]], word+board[ni][nj])

                visited.remove((ni, nj))

        if "$" in curr:
            res.add(word)

        return False

    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] in trie:  # We can start forming the word
                visited.add((i, j))
                dfs(i, j, trie[board[i][j]], board[i][j])
                visited.remove((i, j))

    return list(res)


@time_execution()
def sol_trie_v2(board: list[list[str]], words: list[str]) -> list[str]:
    WIDTH = len(board[0])
    HEIGHT = len(board)
    trie: dict[str, dict] = {}
    for word in words:
        curr = trie
        for c in word:
            if c not in curr:
                curr[c] = {}

            curr = curr[c]

        # Store the word in the final charater's node
        curr["$"] = word

    res = []

    def dfs(i: int, j: int, curr: dict[str, dict]) -> None:
        for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= ni < HEIGHT and 0 <= nj < WIDTH and board[ni][nj] in curr and board[ni][nj] != '.':
                c = board[ni][nj]
                board[ni][nj] = '.'

                dfs(ni, nj, curr[c])

                board[ni][nj] = c

        if "$" in curr:
            res.append(curr["$"])
            curr.pop("$")  # Remove the word so we don't add it again

        return False

    for i in range(HEIGHT):
        for j in range(WIDTH):
            c = board[i][j]
            if c in trie:
                board[i][j] = '.'
                dfs(i, j, trie[c])
                board[i][j] = c

    return res
