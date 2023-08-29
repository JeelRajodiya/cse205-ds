from typing import List


class Solution:

    def findNumbers(self, nums: List[int]) -> int:
        numsStr = map(lambda a: str(a), nums)
        ans = 0
        for i in numsStr:
            if len(i) % 2 == 0:
                ans += 1
        return ans