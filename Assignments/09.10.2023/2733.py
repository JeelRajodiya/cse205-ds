from typing import List


class Solution:

    def findNonMinOrMax(self, nums: List[int]) -> int:

        nums = list(set(nums))
        if len(nums) <= 2:
            return -1
        nums.sort()

        return nums[1]
