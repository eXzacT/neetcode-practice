if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string. 
    Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.'''


@time_execution()
def sol(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    res = [0] * (len(num1) + len(num2))

    for i in range(len(num1) - 1, -1, -1):
        for j in range(len(num2) - 1, -1, -1):
            product = int(num1[i]) * int(num2[j]) + res[i+j+1]
            res[i+j] += product//10  # Serves as carry for next iteration
            res[i+j+1] = product % 10  # Remainder

    return ''.join(map(str, res)).lstrip('0')


@time_execution()
def sol_v2(num1: str, num2: str) -> str:
    res = 0

    for i in range(len(num2)-1, -1, -1):
        carry = temp = 0
        for j in range(len(num1)-1, -1, -1):
            product = int(num1[j]) * int(num2[i]) + carry
            carry, remainder = divmod(product, 10)
            temp = temp + remainder * 10**(len(num1)-j-1)

        if carry:
            temp = temp + carry * 10**len(num1)
        res = res + temp * 10**(len(num2)-i-1)

    return str(res)
