if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''There is an integer array nums sorted in ascending order (with distinct values).
    The array could be rotated, for example [0,1,2,4,5,6,7] 
    might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Find the index of a needle in the array with O(log n) runtime complexity, if it doesn't exist return -1'''


@time_execution()
def sol_pivot(arr: list[int], needle: int) -> int:
    l, r = 0, len(arr)-1
    pivot_idx, pivot_val = 0, arr[0]

    while l <= r:
        m = l+(r-l)//2
        if arr[m] == needle:
            return m
        if arr[l] < arr[r]:  # Part of the array from l to r is sorted but not necessarily includes the pivot
            if arr[l] < pivot_val:
                pivot_idx = l
                pivot_val = arr[l]
            break

        # Update current val to be the pivot if it's smaller than what we thought was pivot, also remember idx
        if arr[m] < pivot_val:
            pivot_val = arr[m]
            pivot_idx = m
        # We are in left sorted part
        if arr[m] >= arr[l]:
            l = m+1
        else:
            r = m-1

    # The array ranges from pivot val to the value from the left of it
    if needle < pivot_val or needle > arr[pivot_idx-1]:
        return -1

    # Now that we know where the pivot is we can do a regular binary search on the correct part
    if needle >= pivot_val and needle <= arr[-1]:
        l, r = pivot_idx, len(arr)-1
        while l <= r:
            m = l+(r-l)//2
            if arr[m] == needle:
                return m
            if needle < arr[m]:
                r = m-1
            else:
                l = m+1
    else:
        l, r = 0, pivot_idx-1
        while l <= r:
            m = l+(r-l)//2
            if arr[m] == needle:
                return m
            if needle < arr[m]:
                r = m-1
            else:
                l = m+1

    return -1


@time_execution()
def sol_optimized(arr: list[int], needle: int) -> int:
    l, r = 0, len(arr)-1

    while l <= r:
        m = l+(r-l)//2
        if arr[m] == needle:
            return m

        if arr[m] >= arr[l]:  # Left partition
            # Needle is either in the same partition but right side, or in the right partition(which is also right side)
            if needle > arr[m] or needle < arr[l]:
                l = m+1
            else:  # Stay in left partition
                r = m-1
        else:  # Right partition
            # Needle is either in the same partition but left side, or in the left partition(which is also left side)
            if needle < arr[m] or needle > arr[r]:
                r = m-1
            else:  # Stay in the right partition
                l = m+1

    return -1
