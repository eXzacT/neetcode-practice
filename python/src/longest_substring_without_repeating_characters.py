if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given a string s, find the length of the longest substring without repeating characters.'''


@time_execution()
def sol_naive(s: str) -> int:
    if not s:
        return 0

    substr = set()
    res = 0

    for i in range(len(s)):
        count = 1
        substr.add(s[i])
        for j in range(i+1, len(s)):
            if s[j] in substr:
                res = max(res, len(substr))
                substr.clear()
                break

            count += 1
            substr.add(s[j])

    return max(res, count)


@time_execution()
def sol_optimized(s: str) -> int:
    if not s:
        return 0

    res, l, r = 0, 0, 1
    curr_substr: dict[str, int] = {s[0]: 0}  # char and index
    while r < len(s):
        if s[r] in curr_substr:  # When we encounter a duplicate, move the left pointer just right of it
            l = curr_substr[s[r]]+1
            res = max(len(curr_substr), res)
            curr_substr.clear()  # Reset dictionary and add starting character and its position
            curr_substr[s[l]] = l
            if l < len(s)-1:
                r = l+1

        curr_substr[s[r]] = r
        r += 1

    return max(res, len(curr_substr))


@time_execution()
def sol_optimized_v2(s: str) -> int:
    res = l = r = 0
    curr_substr = set()

    while r < len(s):
        if s[r] in curr_substr:  # When we encounter a duplicate, move the left pointer just right of the original character
            res = max(res, len(curr_substr))
            while s[l] != s[r]:  # We do that by removing all the characters on the left until we reach the duplicate
                curr_substr.remove(s[l])
                l += 1
            # All the other characters are kept as a valid substring, even the duplicate one(but on the right side now)
            l += 1

        curr_substr.add(s[r])
        r += 1

    # In case we didn't find any duplicates in the ending substring then it will still be contained in curr_substr
    return max(res, len(curr_substr))


@time_execution()
def sol_optimized_v3(s: str) -> int:
    l = res = 0
    curr_substr = set()

    for r in range(len(s)):
        # When we encounter a duplicate, move the left pointer just right of that original duplicate
        while s[r] in curr_substr:
            curr_substr.remove(s[l])
            l += 1

        curr_substr.add(s[r])
        res = max(res, r-l+1)

    return res
