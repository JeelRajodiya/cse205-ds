class MyCircularQueue:

    def __init__(self, k: int):
        self.l = [-1] * k
        self.frontIndex = -1
        self.backIndex = -1
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.frontIndex = 0
        self.backIndex = (self.backIndex + 1) % self.size
        self.l[self.backIndex] = value

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.frontIndex == self.backIndex:
            self.frontIndex = -1
            self.backIndex = -1
        else:
            self.frontIndex = (self.frontIndex + 1) % self.size
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.l[self.frontIndex]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.l[self.backIndex]

    def isEmpty(self) -> bool:
        return self.frontIndex == -1

    def isFull(self) -> bool:

        return ((self.backIndex + 1) % self.size) == self.frontIndex


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()