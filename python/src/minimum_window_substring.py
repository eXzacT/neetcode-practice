if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such 
    that every character in t (including duplicates) is included in the window. 
    If there is no such substring, return the empty string "".
    
Note:
    The testcases will be generated such that the answer is unique.'''


@time_execution()
def sol_naive(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""

    t_count = {}
    for c in t:
        t_count[c] = t_count.get(c, 0)+1

    substrings = [s[i: j]
                  for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
    substr_count = {}
    min_substr = ""

    for substr in substrings:
        for c in substr:
            if c in t_count:  # We only care about chars that are also in t
                substr_count[c] = substr_count.get(c, 0)+1

        # Only update if we didn't have a min substr or if we found a smaller one
        if not min_substr or len(substr) < len(min_substr):
            # If both substring and t have same counts of all chars in t
            if all(substr_count.get(c, 0) >= t_count[c] for c in t_count):
                min_substr = substr

        substr_count.clear()

    return min_substr


@time_execution()
def sol_better(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""

    t_count = {}
    for c in t:
        t_count[c] = t_count.get(c, 0)+1

    s_count = {}
    min_substr = ""
    l = 0
    for r in range(len(s)):
        if s[r] in t_count:  # We only care if the character exists in t
            s_count[s[r]] = s_count.get(s[r], 0)+1

            # If we have a match, keep moving left pointer right until we stop having one, so we can find the shortest length
            while all(s_count.get(c, 0) >= t_count[c] for c in t):
                if not min_substr or len(min_substr) > r-l:
                    min_substr = s[l:r+1]
                if s[l] in s_count:
                    s_count[s[l]] -= 1
                l += 1

    return min_substr


@time_execution()
def sol_optimized(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""

    s_count = {}
    t_count = {}
    for c in t:
        t_count[c] = t_count.get(c, 0)+1

    matches = l = 0
    res = (-1, -1)  # Indices of left and right pointers

    for r in range(len(s)):
        # Only care about characters that are in t
        if s[r] in t:
            # Add the character at right pointer, if we now have same count for that character increment matches
            s_count[s[r]] = s_count.get(s[r], 0)+1
            if s_count[s[r]] == t_count[s[r]]:
                matches += 1

        # Have all the characters from t in s, keep moving left pointer right to decrease substring while keeping it valid
        while matches == len(t_count):
            # First time we're setting min substring or found lower
            if res[1]-res[0] == 0 or r-l < res[1]-res[0]:
                res = (l, r+1)

            if s[l] in t:  # Ignore characters that are not in t
                # Already had the right count, but about to remove it so there will be a mismatch
                if s_count[s[l]] == t_count[s[l]]:
                    matches -= 1
                s_count[s[l]] -= 1

            l += 1

    l, r = res
    return s[l:r] if r-l else ""
