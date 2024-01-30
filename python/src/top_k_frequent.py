import itertools
from collections import Counter

if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution


@time_execution()
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    counter = Counter(nums)
    return [key for key, _ in counter.most_common(k)][:k]


@time_execution()
def top_k_frequent_optimized(nums: list[int], k: int) -> list[int]:
    count = {}
    max_count = 0
    for num in nums:
        c = count.get(num, 0)+1
        if c > max_count:
            max_count = c
        count[num] = c

    freq = [[] for _ in range(len(nums)+1)]
    for num, count in count.items():
        freq[count].append(num)

    return list(itertools.chain(*freq[max_count::-1]))[:k]


if __name__ == "__main__":
    nums = [5, 3, 1, 1, 1, 3, 73, 1]
    k = 2

    print(top_k_frequent(nums, k))
    print(top_k_frequent_optimized(nums, k))
