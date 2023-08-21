from typing import List


class Solution:

    def recursion(self, ans: List[str], s: str, l: int, r: int, n: int):
        if (l + r == 2 * n):
            ans.append(s)
            return
        if (l < n):

            self.recursion(ans, s + "(", l + 1, r, n)
        if (r < l):

            self.recursion(ans, s + ")", l, r + 1, n)

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.recursion(ans, "", 0, 0, n)
        return ans
