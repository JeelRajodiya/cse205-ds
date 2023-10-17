from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}
        for n, i in enumerate(nums):
            hashMap[i] = n

        for n, i in enumerate(nums):
            secondIndex = hashMap.get(target - i)

            if secondIndex != None and secondIndex != n:
                return [secondIndex, n]
        return [-1, -1]
