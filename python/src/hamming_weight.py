if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has 
    (also known as the Hamming weight).'''


@time_execution()
def sol(num: int) -> int:
    return num.bit_count()


@time_execution()
def sol_v2(num: int) -> int:
    res = 0
    while num:
        res += num % 2
        num //= 2

    return res


@time_execution()
def sol_v3(num: int) -> int:
    res = 0
    while num:
        res += num % 2
        num >>= 1

    return res


@time_execution()
def sol_v4(num: int) -> int:
    res = 0
    for c in str(bin(num)):
        if c == "1":
            res += 1

    return res


@time_execution()
def sol_v5(num: int) -> int:
    res = 0
    while num:
        # Every time we do this operation there will be 1 less '1' in the number
        res += 1
        num &= (num-1)

    return res
