if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given a string 's', return the longest palindromic substring in 's'.'''


@time_execution()
def sol_naive(s: str) -> str:
    res = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                if len(s[i:j]) > len(res):
                    res = s[i:j]
    return res


@time_execution()
def sol_optimized(s: str) -> str:
    res = ""
    for i in range(len(s)):
        l = r = i
        # Odd palindromes
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if len(s[l:r+1]) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1

        # Even palindromes
        l, r = i, i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if len(s[l:r+1]) > len(res):
                res = s[l:r+1]
            l -= 1
            r += 1

    return res


@time_execution()
def sol_optimized_v2(s: str) -> str:
    res = ""
    l = r = 0
    while r < len(s):
        # Step 1. find identical consecutive characters
        while r < len(s) and s[l] == s[r]:
            r += 1
        if r-l > len(res):
            res = s[l:r]

        # Step 2. use this sequence of identical characters as the center to build palindromes
        ext_left = l - 1
        ext_right = r
        while ext_left >= 0 and ext_right < len(s) and s[ext_left] == s[ext_right]:
            if len(s[ext_left:ext_right+1]) > len(res):
                res = s[ext_left:ext_right+1]
            ext_left -= 1
            ext_right += 1

        l = r  # Left is at the first position where r stopped being same as l

    return res
