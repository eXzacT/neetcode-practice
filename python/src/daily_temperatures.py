if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given an array of integers which represent daily temperatures,
    return another array where at each index we have a counter which counts how many times we need to go
    forward for the temperature to be larger than it is currently.'''


@time_execution()
def sol_naive(temperatures: list[int]) -> list[int]:
    res = []
    for i in range(len(temperatures)):
        for j in range(i+1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                res.append(j-i)
                break
        else:  # If there was no larger temperature, then insert 0
            res.append(0)

    return res


@time_execution()
def sol_optimized(temperatures: list[int]) -> list[int]:
    res = [0]*len(temperatures)
    stack: list[tuple[int, int]] = []
    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            _, idx = stack.pop()
            res[idx] = i-idx

        stack.append((temp, i))

    return res


@time_execution()
def sol_optimized_no_stack(temperatures: list[int]) -> list[int]:
    hottest = 0
    res = [0] * len(temperatures)

    # Going backwards in the list, whenever we find a higher temperature we can update and skip that part
    # Because we will never reach a higher temperature than this one going forward as we've already checked
    for day in range(len(temperatures) - 1, -1, -1):
        temp = temperatures[day]
        if temp >= hottest:
            hottest = temp
        else:  # Initialize difference as 1, but keep increasing while the next temp is larger
            diff = 1
            while temperatures[day + diff] <= temp:
                diff += res[day + diff]

            # At the end of the while loop, we will have the distance between current and next bigger val
            res[day] = diff

    return res
