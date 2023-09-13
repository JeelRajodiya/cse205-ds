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
        toAdd = "({["
        myStack = Stack()
        if len(s) % 2 != 0:
            return False
        for i in s:
            if i in toAdd:
                myStack.add(i)
            else:
                popped = myStack.pop()

                if popped != pairs[i] or popped == None:
                    return False

        if myStack.len == 0:
            return True
        else:
            return False