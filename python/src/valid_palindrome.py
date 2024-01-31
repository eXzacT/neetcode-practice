if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given a string s, return true if it is a palindrome, or false otherwise.

Note:
    A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
    and removing all non-alphanumeric characters, it reads the same forward and backward. 
    Alphanumeric characters include letters and numbers.'''


@time_execution()
def sol_naive(s: str) -> bool:
    alphanumeric = "".join(c.lower() for c in s if c.isalnum())
    return alphanumeric == alphanumeric[::-1]


@time_execution()
def sol_two_pointers(s: str) -> bool:
    alphanumeric = "".join(c.lower() for c in s if c.isalnum())
    left = 0
    right = len(alphanumeric)-1

    while left < right:
        if alphanumeric[left] != alphanumeric[right]:
            return False
        left += 1
        right -= 1

    return True


@time_execution()
def sol_two_pointers_optimized(s: str) -> bool:
    left = 0
    right = len(s)-1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True

# built-in isalnum not allowed


@time_execution()
def sol_two_pointers_optimized_custom_isalnum(s: str) -> bool:
    def isalnum(c: str) -> bool:
        return ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')

    left = 0
    right = len(s)-1

    while left < right:
        if not isalnum(s[left]):
            left += 1
            continue
        if not isalnum(s[right]):
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1

    return True
