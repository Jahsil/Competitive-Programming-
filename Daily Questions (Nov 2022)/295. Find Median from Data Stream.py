# using SortedList
from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        
        self.stack = SortedList()

    def addNum(self, num: int) -> None:
        if len(self.stack) == 0:
            self.stack.add(num)
        else:
            self.stack.add(num)
            

    def findMedian(self) -> float:
        if len(self.stack) % 2 != 0:
            mid = int(len(self.stack) // 2)
            return self.stack[mid]
        else:
            mid = int(len(self.stack) / 2)
            return (self.stack[mid] + self.stack[mid - 1])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# USING MIN AND MAX HEAPS --- MUCH MORE EFFIECIENT SOLUTION
class MedianFinder:

    def __init__(self):
        # using min and max heaps
        self.minHeap = [] 
        self.maxHeap = [] 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap ,-1 * num)
        
        if self.minHeap and self.maxHeap and -1 * self.maxHeap[0] > self.minHeap[0]:
            popedVal = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap , -1 * popedVal)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            popedVal = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap , -1 * popedVal)
            
            
        if len(self.minHeap) > len(self.maxHeap) + 1:
            popedVal = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap , -1 * popedVal)

    def findMedian(self) -> float:
        
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        if len(self.minHeap) == len(self.maxHeap):
            median = (self.minHeap[0] + -1 * self.maxHeap[0]) / 2
            return median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
