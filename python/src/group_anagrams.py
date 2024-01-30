'''Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.'''

from collections import Counter, defaultdict
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


@time_execution()
def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = []
    seen = set()
    for i in range(len(strs)):
        group = set()
        ordered_group = []
        if i not in seen:
            seen.add(i)
            ordered_group.append(strs[i])
            group.add(strs[i])

        for j in range(i+1, len(strs)):
            if j not in seen:
                if Counter(strs[i]) == Counter(strs[j]):
                    seen.add(j)
                    ordered_group.append(strs[j])
                    group.add(strs[j])

        if group:
            groups.append(ordered_group)

    return groups


@time_execution()
def group_anagrams_optimized(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for s in strs:
        anagrams[''.join(sorted(s))].append(s)

    return list(anagrams.values())


@time_execution()
def group_anagrams_optimized_v2(strs: list[str]) -> list[list[str]]:
    anagrams = defaultdict(list)
    for s in strs:
        counter = [0]*26
        for c in s:
            counter[ord(c)-ord('a')] += 1

        anagrams[tuple(counter)].append(s)

    return list(anagrams.values())
