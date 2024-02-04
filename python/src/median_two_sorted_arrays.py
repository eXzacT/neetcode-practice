if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given two sorted arrays nums1 and nums2 return the median of the two sorted arrays.'''


@time_execution()
def sol_naive(nums1: list[int], nums2: list[int]) -> int:
    def merge() -> list[int]:
        merged = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        # Whichever has leftover elements, just add them to the end
        merged.extend(nums1[i:]+nums2[j:])
        return merged

    merged = merge()
    # If uneven get middle, if even get sum of 2 middle nums and divide by 2
    quotient, remainder = divmod(len(merged), 2)
    if remainder:
        return merged[quotient]

    return (merged[quotient]+merged[quotient-1])/2


@time_execution()
def sol_optimized(nums1: list[int], nums2: list[int]) -> int:
    merged_len = len(nums1)+len(nums2)
    half_merged_len, odd = divmod(merged_len, 2)

    # Always do binary search on the smaller array
    A, B = nums1, nums2
    if len(B) < len(A):
        A, B = B, A

    lo, hi = 0, len(A)-1

    while True:
        # If mid1 is 1 and half length is 6, mid2 should be 3
        # That's because on index 1, left partition is of length 2, right is then of length 4, but the index is 3
        midA = lo+(hi-lo)//2
        midB = half_merged_len-midA-2

        A_left = A[midA] if midA >= 0 else float('-inf')
        A_right = A[midA+1] if midA+1 < len(A) else float('inf')
        B_left = B[midB] if midB >= 0 else float('-inf')
        B_right = B[midB+1] if midB+1 < len(B) else float('inf')

        # All the numbers in the left partition are smaller than all the numbers in the right partition
        if A_left <= B_right and B_left <= A_right:
            right_min = min(A_right, B_right)
            if odd:
                return right_min
            else:  # Max between last in left partition + min between first in right partition
                return (max(A_left, B_left)+right_min)/2

        # Move mid A pointer somewhere to the left side, this will also automatically move midB to the right
        if A_left > B_right:
            hi = midA-1
        # Move mid A pointer somewhere to the right side, this will also automatically move midB to the left
        else:
            lo = midA+1
