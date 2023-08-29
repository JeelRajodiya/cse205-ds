from typing import List


class Solution:

    def buildArray(self, nums: List[int]) -> List[int]:
        ans = list(range(0, len(nums)))
        for n, i in enumerate(nums):
            ans[n] = nums[nums[n]]
        return ans