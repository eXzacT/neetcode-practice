if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
    The digits are ordered from most significant to least significant in left-to-right order. 
    The large integer does not contain any leading 0's.
    Increment the large integer by one and return the resulting array of digits.'''


@time_execution()
def sol(digits: list[int]) -> list[int]:
    i = len(digits)-1
    new_digits = digits[:]

    while i >= 0:
        if digits[i] < 9:
            new_digits[i] = digits[i]+1
            break
        else:
            new_digits[i] = 0
        i -= 1
    else:  # There were no breaks which means we still have a remainder
        return [1]+new_digits

    return new_digits


@time_execution()
def sol_v2(digits: list[int]) -> list[int]:
    s = ''.join(str(i)for i in digits)
    return [int(i)for i in str(int(s)+1)]


@time_execution(executions=1)  # Mutating original list, so 1 execution
def sol_v3(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits

    return [1] + digits
