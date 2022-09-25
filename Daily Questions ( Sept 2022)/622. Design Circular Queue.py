class MyCircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.front = 0
        self.rear = 0
        self.k = k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear += 1 
        self.rear %= self.k
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front += 1
        self.front %= self.k
        self.count -= 1
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        if self.rear == self.front and self.count == 0:
            return True 
        return False
        
    def isFull(self) -> bool:
        if self.rear == self.front and self.count == self.k:
            return True
        return False
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
