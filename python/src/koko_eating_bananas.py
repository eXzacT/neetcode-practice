from math import ceil, sqrt
if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

'''Given a list of banana piles and 'h' hours to eat them before guards come back.
    You can decide how many bananas you want to eat per hour, you cannot change that speed later on.
    If you decide to 20 bananas per hour and a pile has 10 bananas, you have to rest for the remaining hour.
    What is the minimum banana eating speed per hour to be able to eat all of the bananas in 'h' hours.'''


@time_execution()
def sol_naive(piles: list[int], h: int) -> int:
    # Not possible to eat everything
    if len(piles) > h:
        return 0

    # Biggest pile is same as the time we have, have to eat that many per hour
    hi = max(piles)
    if h == len(piles):
        return hi

    for speed in range(1, hi):
        remaining = h
        for bananas in piles:
            hours_to_eat = ceil(bananas/speed)
            remaining -= hours_to_eat
            if remaining < 0:
                break  # Early return because we can't eat all the bananes in time, and return falsy value
        else:  # Managed to eat all the bananas before time ran out
            return speed


@time_execution()
def sol_better(piles: list[int], h: int) -> int:
    def time_to_eat(speed: int) -> int:
        if speed <= 0:
            return 0

        remaining = h
        for bananas in piles:
            hours_to_eat = ceil(bananas/speed)
            remaining -= hours_to_eat
            if remaining < 0:
                return 0  # Early return because we can't eat all the bananes in time, and return falsy value
        else:  # Managed to eat all the bananas before time ran out
            return speed

    # Not possible to eat everything
    if len(piles) > h:
        return 0

    # Biggest pile is same as the time we have, have to eat that many per hour
    hi = max(piles)
    if h == len(piles):
        return hi

    jump = int(sqrt(hi))
    curr = jump

    # If the initial check returns true, then keep decreasing curr by jump until it's false, and vice versa
    initial_check = time_to_eat(curr)
    while True:
        if initial_check:
            curr -= jump
        else:
            curr += jump

        next_check = time_to_eat(curr)
        if next_check != initial_check:
            break

    # Now we know the interval where True goes to False or vice versa, have to find exact place where it changes
    # Increase the speed to go back to the speed that initially gave us true
    if initial_check:
        for speed in range(curr, curr+jump):
            if time_to_eat(speed):
                return speed
    # Decrease the speed until we find get the false, but return speed+1 to make it True again
    else:
        for speed in range(curr, curr-jump-1, -1):
            if not time_to_eat(speed):
                return speed+1


@time_execution()
def sol_optimized(piles: list[int], h: int) -> int:
    # Not possible to eat everything
    if len(piles) > h:
        return 0

    # Biggest pile is same as the time we have, have to eat that many per hour
    hi = max(piles)
    if h == len(piles):
        return hi

    lo = 1
    min_speed = hi
    while lo <= hi:
        speed = lo+(hi-lo)//2
        if sum(ceil(bananas/speed) for bananas in piles) <= h:
            min_speed = min(hi, speed)
            hi = speed-1
        else:
            lo = speed+1

    return min_speed
