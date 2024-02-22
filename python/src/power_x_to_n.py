if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Implement pow(x, n), which calculates x raised to the power n'''


@time_execution()
def sol_rec(x: float, n: int) -> float:
    def helper(n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1

        quotient, remainder = divmod(n, 2)
        res = helper(quotient)
        return res*res*helper(remainder)

    return round(helper(n), 5) if n >= 0 else round(1/helper(abs(n)), 5)
