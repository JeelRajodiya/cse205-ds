class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for i in s:

            if i == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(i)

        for i in t:

            if i == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        print(stack1, stack2)
        return stack1 == stack2


sol = Solution()
s = "y#fo##f"
t = "y#f#o##f"

print(sol.backspaceCompare(s, t))
