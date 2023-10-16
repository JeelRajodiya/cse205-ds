from typing import List


class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        m = {}
        sumX = 0
        for i in nums:
            sumX += i

            if i in m:
                m[i] += 1
            else:
                m[i] = 1
        duplicate = 0
        for o in m:
            if m[o] >= 2:
                duplicate = o
        n = len(nums)
        allSum = (n * (n + 1)) / 2
        missing = int(allSum - (sumX - duplicate))
        return [duplicate, missing]
