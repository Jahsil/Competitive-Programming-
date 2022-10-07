from sortedcontainers import SortedList
class MyCalendarThree:

    def __init__(self):
        self.mx = 0
        self.arr = SortedList()

    def book(self, start: int, end: int) -> int:
        self.arr.add((start , 1))
        self.arr.add((end , -1))
        count = 0 
        for x , y in self.arr:
            count += y
            self.mx = max(self.mx , count)
        return self.mx


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
