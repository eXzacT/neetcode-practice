if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given an integer n, return an array of length n + 1 such that for every digit from 0 up to incl n we count their 1 bits'''


@time_execution()
def sol(num: int) -> list[int]:
    return [num.bit_count() for num in range(num+1)]


@time_execution()
def sol_v2(num: int) -> list[int]:
    def count_1_bits(num: int) -> int:
        count = 0
        while num:
            count += num % 2
            num >>= 1
        return count

    return [count_1_bits(num) for num in range(num+1)]


@time_execution()
def sol_v3(num: int) -> list[int]:
    def count_1_bits(num: int) -> int:
        count = 0
        while num:
            count += 1
            num &= num-1
        return count

    return [count_1_bits(num) for num in range(num+1)]


@time_execution()
def sol_dp(num: int) -> list[int]:
    dp = [1]*(num+1)
    dp[0] = 0
    for i in range(2, num+1):
        if (i & (i - 1)) == 0:  # Remember closest power of 2
            closest = i
        else:  # Not a power of 2, needs to use more than 1 bit
            # How many digits we had to use for closest power of 2 + how many for remainder
            dp[i] = 1+dp[i-closest]

    return dp


@time_execution()
def sol_dp_v2(num: int) -> list[int]:
    dp = [1]*(num+1)
    dp[0] = 0
    offset = 2

    for i in range(2, num+1):
        if offset*2 == i:  # Remember closest power of 2
            offset = i
        else:  # Not a power of 2, needs to use more than 1 bit
            # How many digits we had to use for closest power of 2 + how many for remainder
            dp[i] = 1+dp[i-offset]

    return dp
