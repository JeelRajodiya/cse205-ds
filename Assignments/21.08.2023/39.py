from typing import List


class Solution:

    def recursion(self, candidates: List[int], target: int,
                  ans: List[List[int]], tempArr: List[int], it: int):

        if (sum(tempArr) == target):
            ans.append(tempArr.copy())
            return
        if it == len(candidates) or sum(tempArr) > target:
            return
        for i in range(it, len(candidates)):
            tempArr.append(candidates[i])
            self.recursion(candidates, target, ans, tempArr,
                           i)  # Reuse the current candidate
            tempArr.pop()

        # tempArr.pop()

    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:

        ans = []
        self.recursion(candidates, target, ans, [], 0)
        return ans


s = Solution()
print(s.combinationSum([2, 3, 5], 8))
