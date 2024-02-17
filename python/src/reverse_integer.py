import math
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value 
    to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).'''


@time_execution()
def sol(num: int) -> int:
    if num >= 0:
        reverse = int(str(num)[::-1])
    else:
        reverse = -int(str(num)[1:][::-1])

    return reverse if -(2**31) < reverse < (2**31)-1 else 0


@time_execution()
def sol_v2(num: int) -> int:
    MIN = -(2**31)
    MAX = 2**31 - 1

    res = 0
    while num:
        digit = math.fmod(num, 10)
        num = int(num/10)

        # Check for positive overflow
        if res > MAX // 10 or (res == MAX // 10 and digit > 7):
            return 0
        # Check for negative overflow
        if res < MIN // 10 or (res == MIN // 10 and digit < -8):
            return 0

        res = res * 10 + digit

    return res


@time_execution()
def sol_v3(num: int) -> int:
    MIN = -(2**31)
    MAX = 2**31 - 1

    negative = num < 0
    num = abs(num)

    res = 0
    num_str = str(num)
    min_str = str(abs(MIN))
    max_str = str(MAX)

    num_len = len(num_str)
    max_len = len(max_str)

    if num_len > max_len:
        return 0
    possible_overflow = num_len == max_len

    if possible_overflow:
        i = 0  # Current digit
        found_smaller = False
        while num:
            digit = math.fmod(num, 10)
            num = int(num/10)
            # Digit is bigger and we didn't find any digits that were smaller before
            if not found_smaller and digit > int(max_str[i]) and digit > int(min_str[i]):
                return 0
            # We know it will never overflow since a digit was smaller
            if not found_smaller and digit < int(max_str[i]) and digit < int(min_str[i]):
                found_smaller = True

            res = res * 10 + digit
            i += 1
    else:
        while num:
            digit = math.fmod(num, 10)
            num = int(num/10)
            res = res * 10 + digit

    res = int(res)
    return -res if negative else res
