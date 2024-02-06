if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''There are n cars going to the same destination which is 'target' miles away.
    You are given two arrays, one of them represents position and the other represents speed.
    A car can never pass another car ahead of it, even if it's faster.
    The faster car will slow down to match the speed of a slower car in front of it.
    The distance between these two cars is ignored (i.e., they are assumed to have the same position).
    
    A car fleet is some non-empty set of cars driving at the same position and same speed, single car counts too.
    Return the number of car fleets that will arrive at the destination.'''


@time_execution()
def sol_nlogn(target: int, positions: list[int], speeds: list[int]) -> int:
    cars = [(pos, speed) for pos, speed in zip(positions, speeds)]

    # Sort by positions in a descending order
    cars.sort(key=lambda x: x[0], reverse=True)

    res = 0
    pos, speed = cars[0]
    slowest = (target-pos)/speed
    for pos, speed in cars:
        current = (target-pos)/speed
        # Slowest car is still the bottleneck
        if current <= slowest:
            continue
        else:
            res += 1
            slowest = current

    return res+1  # +1 for the initial fleet
