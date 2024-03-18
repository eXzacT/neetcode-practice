''' The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

    Implement the MedianFinder class:

    MedianFinder() 
        initializes the MedianFinder object.
    
    void addNum(int num) 
        adds the integer num from the data stream to the data structure.
    
    double findMedian() 
        returns the median of all elements so far. 
        Answers within 10-5 of the actual answer will be accepted.'''

from heapq import heappop, heappush


class MedianFinderNaive:
    def __init__(self):
        self.numbers = []

    def addNum(self, num: int) -> None:
        self.numbers.append(num)
        self.numbers.sort()

    def findMedian(self) -> float:
        return self.numbers[len(self.numbers)//2] if len(self.numbers) % 2 else (self.numbers[len(self.numbers)//2-1] + self.numbers[len(self.numbers)//2]) / 2


class MedianFinder:
    def __init__(self):
        self.heap = []

    def addNum(self, num: int) -> None:
        heappush(self.heap, num)

    def findMedian(self) -> float:
        temp = self.heap.copy()

        if len(temp) % 2 == 1:
            for _ in range(len(temp)//2):
                heappop(temp)
            return temp[0]
        else:
            for _ in range(len(temp)//2):
                last = heappop(temp)

            return (last+temp[0])/2


class MedianFinderV2:
    def __init__(self):
        self.small_heap = []  # Small heap will be a max heap
        self.large_heap = []  # Large heap will be a min heap

    def addNum(self, num: int) -> None:
        heappush(self.small_heap, -num)
        if self.small_heap and self.large_heap and (-self.small_heap[0] > self.large_heap[0]):
            heappush(self.large_heap, -heappop(self.small_heap))

        # Balance the heaps so that their size difference is no more than 1
        if len(self.small_heap) > len(self.large_heap) + 1:
            heappush(self.large_heap, -heappop(self.small_heap))
        elif len(self.large_heap) > len(self.small_heap) + 1:
            heappush(self.small_heap, -heappop(self.large_heap))

    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        elif len(self.large_heap) > len(self.small_heap):
            return self.large_heap[0]
        else:
            return (-self.small_heap[0] + self.large_heap[0]) / 2
