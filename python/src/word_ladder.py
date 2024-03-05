import networkx as nx
from collections import deque

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''  Given two words, 's1' and 's2', and a list 'words', return count of how many transformations we need to do to transform 's1' into 's2'.

        To transform one word into another one we are only allowed to change a single letter.
        So to go from 'cat' to 'bar' we first need to transform 'cat' into 'bat' and then into 'bar'(both bat and bar need to be in the list)
        's1' doesn't need to be in the list 'words' but 's2' does.'''


def one_char_diff(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    diff_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
        if diff_count > 1:
            return False

    return True


@time_execution()
def sol_dfs(s1: str, s2: str, words: list) -> int:
    seen = set()

    def helper(curr: str) -> int:
        if curr == s2:
            return 1

        min_transforms = float('inf')
        for word in words:
            if word in seen or word == curr:
                continue

            if one_char_diff(word, curr):
                seen.add(word)
                min_transforms = min(min_transforms, 1 + helper(word))
                seen.remove(word)

        return min_transforms

    res = helper(s1)
    return res if res != float('inf') else 0


@time_execution()
def sol_bfs(s1: str, s2: str, words: list) -> int:
    words_set = set(words)
    if s2 not in words_set:
        return 0

    queue = deque([(s1, 1)])
    while queue:
        curr, length = queue.popleft()
        if curr == s2:
            return length

        for i in range(len(curr)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                # Generate a word that only has 1 different character and is of same length
                next_word = curr[:i] + c + curr[i+1:]
                if next_word in words_set:
                    queue.append((next_word, length + 1))
                    words_set.remove(next_word)

    return 0


@time_execution()
def sol_bfs_v2(s1: str, s2: str, words: list) -> int:
    words_set = set(words)
    if s2 not in words_set:
        return 0

    queue = deque([s1])
    length = 1

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()
            if curr == s2:
                return length

            for i in range(len(curr)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    # Generate a word that only has 1 different character and is of same length
                    next_word = curr[:i] + c + curr[i+1:]
                    if next_word in words_set:
                        queue.append(next_word)
                        words_set.remove(next_word)

        length += 1

    return 0


@time_execution()
def sol_two_sets(s1: str, s2: str, words: list) -> int:
    if s2 not in (words_set := set(words)):
        return 0

    words1, words2 = set((s1, )), set((s2, ))
    words_set.discard(s1)
    words_set.discard(s2)
    counts = 2  # Start the count from 2 since we have s1 and s2

    while words1 and words2:
        # We're doing BFS from the smaller set and matching a larger set(bigger chance of hitting the result)
        if len(words1) > len(words2):
            words1, words2 = words2, words1

        temp = set()
        for word in words1:  # For every word in the first set we traverse to its next word, basically BFS
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i]+c+word[i+1:]
                    if new_word in words2:  # Reached the end
                        return counts
                    # Can transform the word to a new one
                    if new_word in words_set:
                        temp.add(new_word)
                        # First time we see any new words we can remove them from the set since we found the fastest way to get to them
                        words_set.remove(new_word)

        words1 = temp
        counts += 1  # Level of the bfs traversal

    return 0  # Couldn't reach the 's2' word


@time_execution()
def sol_nx(s1: str, s2: str, words: list) -> int:
    if s2 not in words:
        return 0

    G = nx.DiGraph()

    def helper(curr: str, seen: set) -> None:
        for word in words:
            if curr == word or word in seen:
                continue

            seen.add(curr)
            if one_char_diff(word, curr):
                G.add_edge(curr, word)
                helper(word, seen)

    helper(s1, set())

    return 1+nx.shortest_path_length(G, source=s1, target=s2)
