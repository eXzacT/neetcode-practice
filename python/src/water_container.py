if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''You are given an integer array of heights.
    Every height represents a pole, and the distances between poles are the differences in their indices
    Find two poles, such that they can hold the biggest amount of water.

    Note: Slanting the container so the water doesn't leak on either side is not allowed'''


@time_execution()
def sol_naive(heights: list[int]) -> int:
    return max((j-i)*min(heights[i], heights[j]) for i in range(len(heights)) for j in range(i+1, len(heights)))


@time_execution()
def sol_optimized(heights: list[int]) -> int:
    left = 0
    right = len(heights)-1
    max_area = 0
    while left < right:
        max_area = max(max_area, (right-left) *
                       min(heights[left], heights[right]))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area
