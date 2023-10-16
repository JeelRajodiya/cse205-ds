from typing import List


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i in range(len(nums)):
            elem = nums[i]
            if elem in m:
                m[elem].append(i)
            else:
                m[elem] = [i]

        for i in m:
            indices = m[i]
            for i in range(len(indices) - 1):
                e1 = indices[i]
                e2 = indices[i + 1]
                if abs(e2 - e1) <= k:
                    return True
        return False