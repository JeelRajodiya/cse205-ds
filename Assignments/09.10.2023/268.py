from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = 0
        l = nums[-1]

        idx = 0
        for i in range(n, l + 1):
            if nums[idx] != i:
                return i
            idx += 1
        return idx
