if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.'''


@time_execution()
def sol_naive(s: str) -> int:
    res = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                res += 1

    return res


@time_execution()
def sol_optimized(s: str) -> int:
    res = 0
    for i in range(len(s)):
        # Odd palindromes
        left = right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1

        # Even palindromes
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1

    return res


@time_execution()
def sol_optimized_v2(s: str) -> int:
    l = r = res = 0

    while r < len(s):
        # Step 1. find identical consecutive characters
        while r < len(s) and s[l] == s[r]:
            r += 1
        # Formula to get palindrome count for a r-l long string that contains all the same characters
        res += ((r - l) * (r - l + 1)) // 2

        # Step 2. use this sequence of identical characters as the center to build palindromes
        ext_left = l - 1
        ext_right = r
        while ext_left >= 0 and ext_right < len(s) and s[ext_left] == s[ext_right]:
            res += 1
            ext_left -= 1
            ext_right += 1

        l = r  # Move left pointer to where r is since they stopped being equal, this gives us the next possible partition

    return res
