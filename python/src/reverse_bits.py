if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Reverse bits of a given 32 bits unsigned integer.'''


@time_execution()
def sol(num: int) -> int:
    return int(format(num, '032b')[::-1], 2)


@time_execution()
def sol_v2(num: int) -> int:
    res = [0]*32

    for i in range(32):
        res[i] = str(num % 2)
        num >>= 1

    return int(''.join(res), 2)


@time_execution()
def sol_v3(num: int) -> int:
    res = 0

    for i in range(32):
        bit = (num >> i) & 1  # Finding out what the ith bit is
        res = res | bit << (31-i)  # Adding that bit to the reversed place

    return res
