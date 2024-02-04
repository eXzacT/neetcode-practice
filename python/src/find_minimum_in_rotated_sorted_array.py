if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
    For example, the array nums = [0,1,2,4,5,6,7] might become:

    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times, it goes back to it's original state.

Given the sorted rotated array nums of unique elements, return the minimum element of this array.'''


@time_execution()
def sol_naive(nums: list[int]) -> int:
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            continue
        else:  # First time you encounter a number that's smaller, it has to be the minimum
            return nums[i+1]

    # It was sorted already
    return nums[0]


@time_execution()
def sol_optimized(nums: list[int]) -> int:
    lo, hi = 0, len(nums)-1
    res = nums[0]
    while lo <= hi:
        if nums[lo] < nums[hi]:  # Entire array from lo to hi is sorted, but maybe we saw min before
            return min(nums[lo], res)

        mid = lo+(hi-lo)//2
        res = min(res, nums[mid])
        if nums[mid] >= nums[lo]:  # We are in the left sorted part, go right
            lo = mid+1
        else:  # We are in the right sorted part, go left
            hi = mid-1

    return res
