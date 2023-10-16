from typing import List


class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = {}
        result = 0
        for i in nums:
            if i in pairs:
                result += pairs[i]
                pairs[i] += 1
            else:
                pairs[i] = 1

        return result
