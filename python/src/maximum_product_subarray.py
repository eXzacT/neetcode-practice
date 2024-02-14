from math import prod
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an integer array nums, find a subarray that has the largest product, and return the product.'''


@time_execution()
def sol_naive(nums: list[int]) -> int:
    return max(prod(nums[i:j]) for i in range(len(nums)) for j in range(i+1, len(nums)+1))


@time_execution()
def sol_dp(nums: list[int]) -> int:
    res = max(nums)
    curr_max, curr_min = 1, 1
    for num in nums:
        tmp = num*curr_max
        curr_max = max(tmp, num*curr_min, num)
        curr_min = min(tmp, num*curr_min, num)

        res = max(res, curr_max)

    return res


@time_execution()
def sol_naive_rec(nums: list[int]) -> int:
    prods = []

    def helper(i: int, prod: int = 1) -> None:
        if i == len(nums):
            return

        prods.append(x := (prod*nums[i]))
        helper(i+1, x)  # Take
        helper(i+1)  # Don't take, and reset prod back to 1

    helper(0)
    return max(prods)


@time_execution()
def sol_tail_rec(nums: list[int]) -> int:
    def helper(i: int, min_prod: int, max_prod: int, res: int) -> None:
        if i == len(nums):
            return max(res, max_prod)

        tmp = max_prod*nums[i]
        max_prod = max(tmp, nums[i]*min_prod, nums[i])
        min_prod = min(tmp, nums[i]*min_prod, nums[i])

        return helper(i+1, min_prod, max_prod, max(max_prod, res))

    return helper(0, 1, 1, max(nums))
