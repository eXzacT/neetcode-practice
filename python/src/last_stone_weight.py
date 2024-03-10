if __name__ == "__main__":
    from common import time_execution
else:
    from src.common import time_execution

''' You are given an array of integers 'stones' where stones[i] is the weight of the ith stone.

    We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. 
    If x == y, both stones are destroyed
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

    At the end of the game, there is at most one stone left.
    Return the weight of the last remaining stone. If there are no stones left, return 0.'''

from heapq import heappop, heappush


@time_execution()
def sol(stones: list[int]) -> int:
    heap = []
    for stone in stones:
        heappush(heap, -stone)

    while len(heap) > 1:
        heaviest_stone = heappop(heap)
        second_heaviest_stone = heappop(heap)
        if heaviest_stone == second_heaviest_stone:
            continue
        else:
            heappush(heap, -abs(heaviest_stone - second_heaviest_stone))

    return -heap[0] if heap else 0


class MaxHeap:
    def __init__(self, array: list[int]):
        self.heap = []
        for num in array:
            self.push(num)

    def __len__(self):
        return len(self.heap)

    def push(self, num: int):
        self.heap.append(num)
        self.heapify_up()

    def pop(self) -> int:
        self.swap(0, -1)
        el = self.heap.pop()
        # self.heapify_down_rec(0)
        self.heapify_down()
        return el

    def swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self):
        i = len(self.heap) - 1
        parent = (i-1)//2
        while i > 0 and self.heap[i] > self.heap[parent]:
            self.swap(i, parent)
            i = parent
            parent = (i-1)//2

    def heapify_down(self):
        parent = 0

        while parent < len(self.heap):
            i = min((parent, parent*2+1, parent*2+2),
                    key=lambda x: self.heap[x] if x < len(self.heap) else float('inf'))

            if i == parent:
                break

            self.swap(i, parent)
            parent = i

    def heapify_down_rec(self, idx: int):
        i = min((idx, idx*2+1, idx*2+2),
                key=lambda x: self.heap[x] if x < len(self.heap) else float('inf'))

        if i == idx:
            return

        self.swap(idx, i)
        self.heapify_down_rec(i)


@time_execution()
def sol_nolib(stones: list[int]) -> int:
    heap = MaxHeap(stones)

    while len(heap) > 1:
        heaviest_stone = heap.pop()
        second_heaviest_stone = heap.pop()
        if heaviest_stone == second_heaviest_stone:
            continue
        else:
            heap.push(abs(heaviest_stone - second_heaviest_stone))

    return heap.pop() if heap else 0
