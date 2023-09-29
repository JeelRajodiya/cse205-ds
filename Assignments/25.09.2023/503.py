from typing import List


class Solution:

    def nextGreaterElements(self, nums1: List[int]) -> List[int]:

        res = [-1] * len(nums1)
        stack = []

        n = len(nums1)
        nums1 = nums1 * 2

        for i in range(n * 2):
            while stack and nums1[stack[-1]] < nums1[i]:
                idx = stack.pop()
                res[idx] = nums1[i]
            if i < n:
                stack.append(i)

        return res
