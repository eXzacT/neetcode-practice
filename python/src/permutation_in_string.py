import string
from itertools import permutations
from collections import Counter

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.'''


@time_execution()
def sol_naive_functional(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    return any(''.join(perm) in s2 for perm in permutations(s1))


@time_execution()
def sol_window_naive(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    l, r = 0, len(s1)
    counter = Counter(s1)
    while r <= len(s2):
        if Counter(s2[l:r]) == counter:
            return True
        l += 1
        r += 1

    return False


@time_execution()
def sol_window_optimized(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    count1 = {}
    count2 = {}
    l = r = 0

    # Populate counter for s1
    for c in s1:
        count1[c] = count1.get(c, 0)+1

    for r in range(len(s2)):
        if s2[r] in count1:
            if not count2:  # Move left pointer where right is first time we hit
                l = r
            count2[s2[r]] = count2.get(s2[r], 0)+1
            if r-l == len(s1)-1:  # Window size matches, do frequencies match?
                if count2 == count1:
                    return True
                else:  # Decrement count for the character at l and move left pointer once
                    if s2[l] in count2:
                        count2[s2[l]] -= 1
                    l += 1
        else:  # We started populating count2 but broke the substring, empty the count2 dict
            if count2:
                count2.clear()

    return False


@time_execution()
def sol_window_optimized_v2(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    # Count of each character in both strings, but using length of the first string
    count1, count2 = [0]*26, [0]*26
    for i in range(len(s1)):
        count1[ord(s1[i])-ord('a')] += 1
        count2[ord(s2[i])-ord('a')] += 1

    # Max sum of this will be 26, it says which characters both strings do NOT have and which characters they HAVE in equal amounts
    matches = sum(c1 == c2 for c1, c2 in zip(count1, count2))

    for r in range(len(s1), len(s2)):
        if matches == 26:
            return True

        l_idx, r_idx = ord(s2[r-len(s1)])-ord('a'), ord(s2[r])-ord('a')

        # Before removing we check if they're equal, we have to remove it regardless, but if they were equal they won't be anymore
        if count2[l_idx] == count1[l_idx]:
            matches -= 1
        count2[l_idx] -= 1
        if count2[l_idx] == count1[l_idx]:  # Are they the same after removing?
            matches += 1

        # Before adding we check if they're equal, we have to add it regardless, but if they were equal they won't be anymore
        if count2[r_idx] == count1[r_idx]:
            matches -= 1
        count2[r_idx] += 1
        if count2[r_idx] == count1[r_idx]:  # Are they the same after adding?
            matches += 1

    return matches == 26
