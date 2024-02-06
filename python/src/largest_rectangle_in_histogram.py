if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an array of integers heights representing the histogram's bar height where the width of each bar 
    is 1, return the area of the largest rectangle in the histogram.'''


@time_execution()
def sol_naive(heights: list[int]) -> int:
    max_area = heights[0]
    for i in range(1, len(heights)):
        max_area = max(heights[i], max_area)
        min_height = heights[i]
        j = i-1

        # Calculate all the areas while going backwards from the current
        while j >= 0:
            # Minimum height is what's bottlenecking
            min_height = min(min_height, heights[j])
            # Distance between these heights * min
            max_area = max(max_area, (i-j+1)*min_height)
            j -= 1

    return max_area


@time_execution()
def sol_optimized(heights: list[int]) -> int:
    stack = [(0, heights[0])]  # Index and value at that index
    max_area = heights[0]
    for i in range(1, len(heights)):
        start = i
        while stack and heights[i] < stack[-1][1]:
            idx, height = stack.pop()
            # i-idx is the width, how many times we could keep extending the height
            max_area = max(max_area, (i-idx)*height)
            start = idx

        # Only append if that height doesn't already exist or if empty
        if not stack or stack and heights[i] != stack[-1][1]:
            # If we were popping bigger heights, then we have to copyover the index we started counting them
            # That's because we could have had this lower height that entire time underneath it
            stack.append((start, heights[i]))

    # All the heights we didn't pop because they could keep getting extended
    for idx, height in stack:
        max_area = max(max_area, (len(heights)-idx)*height)

    return max_area


@time_execution()
def sol_optimized_v2(heights: list[int]) -> int:
    stack = [(0, heights[0])]  # Index and value at that index
    max_area = heights[0]
    for i in range(1, len(heights)):
        start = i
        while stack and heights[i] < stack[-1][1]:
            idx, height = stack.pop()
            # i-idx is the width, how many times we could keep extending the height
            max_area = max(max_area, (i-idx)*height)
            start = idx

        # If we were popping bigger heights, then we have to copyover the last index of a height we popped,
        # That's because we could have had this lower height that entire time underneath it
        stack.append((start, heights[i]))

    # All the heights we didn't pop because they could keep getting extended
    for idx, height in stack:
        max_area = max(max_area, (len(heights)-idx)*height)

    return max_area
