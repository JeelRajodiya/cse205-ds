class MinStack:

    def __init__(self):
        self.arr = []
        self.min = 0
        self.minStack = []
        self.len = 0

    def __len__(self):
        return self.len

    def push(self, val: int) -> None:
        print(len(self))
        if len(self) == 0:
            self.min = val
        else:

            self.min = min(val, self.min)
        self.minStack.append(self.min)

        self.len += 1
        self.arr.append(val)

    def pop(self) -> None:

        if self.len > 0:
            self.len -= 1
            popped = self.arr.pop()
            self.minStack.pop()
            if len(self.minStack) > 0:
                self.min = self.minStack[-1]
            else:
                self.min = None
            return popped
        assert "Can not pop from empty stack"

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:

        return self.minStack[-1]
