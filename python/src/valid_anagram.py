from collections import Counter, defaultdict
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.
'''


@time_execution()
def valid_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


@time_execution()
def valid_anagram_v2(s: str, t: str) -> bool:
    counter = defaultdict(int)
    for c in s:
        counter[c] += 1
    for c in t:
        counter[c] -= 1

    return all(c == 0 for c in counter.values())


@time_execution()
def valid_anagram_v3(s: str, t: str) -> bool:
    counter = defaultdict(int)
    for c in s:
        counter[c] += 1
    for c in t:
        counter[c] -= 1
        if counter[c] < 0:
            return False

    return all(c == 0 for c in counter.values())
