class Stack():

    def __init__(self) -> None:
        self.arr = []
        self.len = 0

    def pop(self):
        if self.len == 0:
            return None

        self.len -= 1

        return self.arr.pop()

    def peek(self) -> str:
        return self.arr[-1]

    def add(self, v: str) -> None:
        self.len += 1
        self.arr.append(v)


class Solution:

    def isValid(self, s: str) -> bool:

        pairs = {")": "(", "]": "[", "}": "{"}

        myStack = Stack()

        for i in s:
            if i in pairs:
                if myStack.len and myStack.peek() == pairs[i]:
                    myStack.pop()
                else:
                    return False
            else:
                myStack.add(i)

        if myStack.len == 0:
            return True
        else:
            return False