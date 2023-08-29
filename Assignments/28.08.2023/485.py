from typing import List


class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = []
        last = None
        count = 0

        for i in nums:
            if i == 0:
                ans.append(count)
                count = 0
            else:
                count += 1
        ans.append(count)

        return max(ans)
