class MyCircularQueue:

    def __init__(self, k: int):
        self.Q = []
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.Q.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.Q.pop(0)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[0]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.Q[-1]

    def isEmpty(self) -> bool:
        return len(self.Q) == 0

    def isFull(self) -> bool:
        return len(self.Q) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()