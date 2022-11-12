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
