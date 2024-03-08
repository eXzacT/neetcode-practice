''' Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Implement KthLargest class:

        KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
        int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.'''

from heapq import heappush, heappop, heapify


class KthLargestNaive:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        return self.nums[-self.k]


class KthLargestOptimized:
    def __init__(self, k: int, nums: list[int]):
        self.k, self.heap = k, nums
        heapify(self.heap)
        # Keep a heap of k size, the first element will always be kth largest(smallest in k size)
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]


class MinHeap:
    def __init__(self):
        self.heap: list[int] = []

    def __len__(self) -> int:
        return len(self.heap)

    def __repr__(self) -> str:
        return f"<MinHeap: {self.heap}>"

    # Appending to the end and then heapifying up to find where it should belong
    def push(self, val: int):
        self.heap.append(val)
        self.heapify_up()

    def pop(self) -> int | None:
        if not self.heap:
            return None

        # Swap the smallest and biggest nodes, then heapify down
        self.swap(0, len(self.heap) - 1)
        root = self.heap.pop()
        self.heapify_down()

        return root

    def peek(self) -> int:
        return self.heap[0] if self.heap else None

    def swap(self, i: int, j: int):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Move the node we just added up until it's no longer smaller than it's parent
    def heapify_up(self):
        i = len(self.heap) - 1
        while i > 0:
            parent_idx = (i - 1) // 2
            if self.heap[i] < self.heap[parent_idx]:
                self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            i = parent_idx

    def heapify_down(self):
        parent, left, right = 0, 1, 2

        while parent < len(self.heap) - 1:
            smaller = parent
            if left < len(self.heap) and self.heap[left] < self.heap[smaller]:
                smaller = left

            if right < len(self.heap) and self.heap[right] < self.heap[smaller]:
                smaller = right

            if smaller != parent:  # Found a smaller child than the parent, swap them
                self.swap(parent, smaller)

                parent = smaller
                left = 2 * parent + 1
                right = 2 * parent + 2

            else:  # There was no smaller children, heap has the proper structure
                break


class KthLargestOptimizedNoLib:
    def __init__(self, k: int, nums: list[int]):
        self.k, self.heap = k, MinHeap()
        for num in nums:
            self.heap.push(num)

        # Keep a heap of k size, the first element will always be kth largest(smallest in k size)
        while len(self.heap) > k:
            self.heap.pop()

    def add(self, val: int) -> int:
        self.heap.push(val)
        if len(self.heap) > self.k:
            self.heap.pop()

        return self.heap.peek()
