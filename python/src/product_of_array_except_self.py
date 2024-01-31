from functools import reduce
from operator import mul

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an integer array nums, return a new array 
    where every element at index [i] is the product of all the other elements except element at current [i]'''


@time_execution()
def sol_naive(nums: list[int]) -> list[int]:
    new_arr = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]

        new_arr.append(product)

    return new_arr


@time_execution()
def sol_naive_functional(nums: list[int]) -> list[int]:
    return [reduce(mul, [nums[i] for i in range(len(nums)) if i != j]) for j in range(len(nums))]


@time_execution()
def sol_time_optimized(nums: list[int]) -> list[int]:
    # If there's at least 2 zeros it means we will have a product of 0 at every index
    zeros = nums.count(0)
    if zeros >= 2:
        return [0]*len(nums)

    total_product = reduce(mul, [num for num in nums if num])
    # We have 1 zero, then set every position to be 0 except the position where it's actually 0
    if zeros:
        return [0 if nums[i] != 0 else total_product for i in range(len(nums))]

    # At every position we just divide by current number if that number isn't 0 to get product of others
    return [total_product//nums[i] if nums[i] else total_product for i in range(len(nums))]

# Follow up: Division not allowed


@time_execution()
def sol_time_optimized_no_div(nums: list[int]) -> list[int]:
    # Initialize 2 arrays which represent what the product is so far on the left and on the right at each position
    prefix = [1 for _ in range(len(nums))]
    postfix = [1 for _ in range(len(nums))]

    pre = post = 1
    # Skip first, it will stay 1, as there is nothing to multiply with on the left
    for i in range(1, len(nums)):
        prefix[i] = (pre := pre*nums[i-1])

    # Skip last, it will stay 1, as there is nothing to multiply with on the right
    for i in range(len(nums)-2, -1, -1):
        postfix[i] = (post := post*nums[i+1])

    return [prefix[i]*postfix[i] for i in range(len(nums))]

# Follow up: Can you solve the problem in O(1) extra space complexity?
# (The output array does not count as extra space for space complexity analysis.)


@time_execution()
def sol_space_time_optimized(nums: list[int]) -> list[int]:
    pre = post = 1
    res = [1 for _ in range(len(nums))]
    # Skip first, it will stay 1, as there is nothing to multiply with on the left
    for i in range(1, len(res)):
        # res[i] = pre
        # pre *= nums[i]
        res[i] = (pre := pre*nums[i-1])

    # Skip last, it will stay 1, as there is nothing to multiply with on the right
    for i in range(len(res)-2, -1, -1):
        # res[i] *= post
        # post *= nums[i]
        res[i] *= (post := post*nums[i+1])

    return res
