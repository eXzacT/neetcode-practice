from itertools import groupby

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.'''


@time_execution()
def sol_naive(nums: list[int]) -> int:
    sol = 0
    for i in range(len(nums)):
        max_len = 1
        curr = nums[i]+1
        j = 0
        while j < len(nums):
            if nums[j] == curr:
                max_len += 1
                curr += 1
                j = 0
            j += 1

        sol = max(max_len, sol)

    return sol


@time_execution()
def sol_sorted(nums: list[int]) -> int:
    if not nums:
        return 0

    nums = sorted(nums)

    prev_max_len = 0
    max_len = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:  # Same, just skip, we could also turn the list into a set before sorting
            continue
        if nums[i] == nums[i-1]+1:
            max_len += 1
        else:
            prev_max_len = max(max_len, prev_max_len)
            max_len = 0

    return 1+max(max_len, prev_max_len)


@time_execution()
def sol_sorted_groupby(nums: list[int]) -> int:
    return max((len(list(g)) for _, g in groupby(enumerate(sorted(set(nums))), lambda i_x: i_x[0]-i_x[1])), default=0)


@time_execution(executions=1000)
def sol_optimized(nums: list[int]) -> int:
    nums_set = set(nums)
    max_len = 0
    for num in nums_set:
        if num-1 not in nums_set:  # Current number is the leftmost number in a sequence
            curr_len = 0
            # Count the current sequence length and update max if max
            while num+curr_len in nums_set:
                curr_len += 1
            max_len = max(curr_len, max_len)

    return max_len


@time_execution(executions=1000)
def sol_exzact(nums: list[int]) -> int:
    nums_dict = {}
    for num in nums:
        if num not in nums_dict:
            left = nums_dict.get(num - 1, 0)
            right = nums_dict.get(num + 1, 0)
            cur_length = 1 + left + right
            nums_dict[num] = cur_length
            # We only ever care about updating the leftmost and rightmost number of the sequence
            # Because when we add new numbers on each side they need to hold the correct value for this seq
            nums_dict[num - left] = cur_length
            nums_dict[num + right] = cur_length

    return max(nums_dict.values(), default=0)


@time_execution(executions=1000)
def sol_exzact_v2(nums: list[int]) -> int:
    if not nums:
        return 0

    # To cover negative numbers edge cases
    if min(nums) < 0:
        len_list = [0]*(max(nums)+(-min(nums))+2)
    else:
        len_list = [0]*(max(nums)+2)

    for num in nums:
        if not len_list[num]:
            left = len_list[num-1]
            right = len_list[num+1]
            cur_length = 1 + left + right
            len_list[num] = cur_length
            # We only ever care about updating the leftmost and rightmost number of the sequence
            # Because when we add new numbers on each side they need to hold the correct value for this seq
            len_list[num - left] = cur_length
            len_list[num + right] = cur_length

    return max(len_list)


[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
