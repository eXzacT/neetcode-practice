if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' Write an algorithm to determine if a number 'num' is happy.
    A happy number is a number defined by the following process:

        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy.

    Return true if 'num' is a happy number, and false if not.'''


@time_execution()
def sol(num: int) -> bool:
    seen = set()
    while num not in seen:
        seen.add(num)
        num = sum([int(c)**2 for c in str(num)])

    return num == 1


@time_execution()
def sol_v2(num: int) -> bool:
    seen = set()
    while num not in seen:
        seen.add(num)
        new_num = 0
        while num:
            digit = num % 10
            new_num += digit**2
            num //= 10

        num = new_num

    return num == 1


@time_execution()
def sol_space_optimized(num: int) -> bool:
    def get_next(num: int) -> int:
        new_num = 0
        while num:
            num, digit = divmod(num, 10)
            new_num += digit ** 2
        return new_num

    slow = num
    fast = get_next(num)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1
