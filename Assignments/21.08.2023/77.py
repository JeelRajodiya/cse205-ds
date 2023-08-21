from typing import List


class Solution:

    def recursion(self, n: int, k: int, it: int, ans: List[List[int]],
                  temp: List[int]):

        if k == 0:
            ans.append(temp.copy())
            return

        for i in range(it, n + 1):

            temp.append(i)
            self.recursion(n, k - 1, i + 1, ans, temp)
            temp.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []
        temp = []
        self.recursion(n, k, 1, ans, temp)
        return ans


s = Solution()
print(s.combine(5, 2))
