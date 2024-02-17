if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given two integers a and b, return the sum of the two integers without using the operators + and -.'''


@time_execution()
def sol(a: int, b: int) -> int:
    res = carry = i = 0
    while a or b:
        if a % 2 & b % 2 and carry:  # Both bits 1 and carry is 1
            res |= 1 << i
        elif a % 2 & b % 2 and not carry:  # Both bits 1 but didn't have a carry
            carry = 1
        elif a % 2 | b % 2 and not carry:  # One bit 1 and don't have a carry
            res |= 1 << i
        elif not (a % 2 | b % 2) and carry:
            res |= 1 << i
            carry = 0

        a >>= 1
        b >>= 1
        i += 1

    return res | 1 << i if carry else res


@time_execution()
def sol_v2(a: int, b: int) -> int:
    while b != 0:  # Need a while loop because it is possible that our carry gave us a new carry, so keep doing it until there's no carry
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return a


@time_execution()
def sol_v3(a: int, b: int) -> int:
    # Works for negative numbers unlike v1 and v2
    mask = 0xffffffff  # 32 bit integer with all 1s

    while b != 0:
        carry = (a & b) << 1
        a = (a ^ b) & mask
        b = carry & mask

    if a > mask // 2:  # Means a is a binary negative number
        return ~(a ^ mask)  # Convert it to an integer negative number
    else:
        return a
