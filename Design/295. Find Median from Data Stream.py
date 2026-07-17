# heap
# ref: https://leetcode.com/problems/find-median-from-data-stream/discuss/1330646/C%2B%2BJavaPython-MinHeap-MaxHeap-Solution-Picture-explain-Clean-and-Concise


# min heap: heappush, heappop
# max heap: heappush_max, heappop_max
class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heappush_max(self.maxheap, num)
        heappush(self.minheap, heappop_max(self.maxheap))
        if len(self.maxheap) < len(self.minheap):
            heappush_max(self.maxheap, heappop(self.minheap))
        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return self.maxheap[0]
        else:
            return (self.maxheap[0]+self.minheap[0])/2

# or: negate the numbers in max heap to simulate max heap using min heap
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        heappush(self.minHeap, -heappop(self.maxHeap))
        if len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0]+self.minHeap[0])/2

# binary search
class MedianFinder:

    def __init__(self):
        self.array = []
        self.n = 0

    def addNum(self, num: int) -> None:
        insort_left(self.array, num)
        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 1:
            return self.array[self.n//2]
        else:
            return (self.array[(self.n-1)//2]+self.array[(self.n-1)//2+1])/2

# brute force / sort
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        if len(self.arr) % 2 != 0: return self.arr[len(self.arr)//2]
        else: 
            i = len(self.arr)//2
            return (self.arr[i] + self.arr[i-1])/2


# sorted list
from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = SortedList()

    def addNum(self, num: int) -> None:
        self.arr.add(num)

    def findMedian(self) -> float:
        i = len(self.arr)
        if i % 2 != 0: return self.arr[i//2]
        else: return (self.arr[i//2] + self.arr[i//2-1])/2