if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


@time_execution()
def sol_naive(heights: list[int]) -> int:
    area = 0
    for i in range(1, len(heights)-1):
        left_max = max(heights[:i])
        right_max = max(heights[i+1:])
        # Water is spilling over on either side
        if heights[i] > left_max or heights[i] > right_max:
            continue
        # How many squares can we fill above us?
        area += min(left_max, right_max)-heights[i]

    return area


@time_execution()
def sol_time_optimized(heights: list[int]) -> int:
    # Key is index, value is max height for that index
    max_left_heights = {}
    max_right_heights = {}
    max_left_height = heights[0]
    max_right_height = heights[-1]

    for i in range(1, len(heights)):
        max_left_height = max(max_left_height, heights[i])
        max_left_heights[i] = max_left_height

    for i in range(len(heights)-2, -1, -1):
        max_right_height = max(max_right_height, heights[i])
        max_right_heights[i] = max_right_height

    area = 0
    for i in range(1, len(heights)-1):
        # Water is spilling over on either side
        if heights[i] > max_left_heights[i] or heights[i] > max_right_heights[i]:
            continue
        # How many squares can we fill above us?
        area += min(max_left_heights[i], max_right_heights[i])-heights[i]

    return area


@time_execution()
def sol_spill_simulate_naive(heights: list[int]) -> int:
    WIDTH = len(heights)
    max_height_idx, max_height_val = max(
        enumerate(heights), key=lambda x: x[1])
    filled = 0
    heights = heights.copy()  # Not necessary but so we don't edit the previous array

    for d in [-1, 1]:
        curr_idx = max_height_idx
        prev_height = max_height_val
        while 0 <= curr_idx < WIDTH:
            curr_idx += d
            if curr_idx == WIDTH or curr_idx == -1:
                break
            # Water slides over in the same direction
            if heights[curr_idx] == prev_height:
                continue
            # Water falls down to current height
            elif heights[curr_idx] < prev_height:
                prev_height = heights[curr_idx]
            # Water can't go further
            else:
                # Increment count, set the previous position to be higher by 1 and start from highest point again
                filled += 1
                heights[curr_idx-d] += 1
                prev_height = max_height_val
                curr_idx = max_height_idx

    return filled


@time_execution()
def sol_space_time_optimized(heights: list[int]) -> int:
    filled = 0
    left, right = 0, len(heights)-1
    max_left, max_right = heights[left], heights[right]

    while left < right:
        if max_left < max_right:
            left += 1
            if heights[left] > max_left or heights[left] > max_right:
                max_left = max(max_left, heights[left])
                continue

            filled += min(max_left, max_right)-heights[left]
        else:
            right -= 1
            if heights[right] > max_left or heights[right] > max_right:
                max_right = max(max_right, heights[right])
                continue

            filled += min(max_left, max_right)-heights[right]

    return filled


@time_execution()
def sol_space_time_optimized_v2(heights: list[int]) -> int:
    filled = 0
    left, right = 0, len(heights)-1
    max_left, max_right = heights[left], heights[right]

    while left < right:
        if max_left <= max_right:
            left += 1
            max_left = max(max_left, heights[left])
            filled += max_left-heights[left]
        else:
            right -= 1
            max_right = max(max_right, heights[right])
            filled += max_right-heights[right]

    return filled
