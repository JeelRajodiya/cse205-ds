from typing import List


class Solution:

    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
        res = [x for i, x in sorted(sorted_nums[-k:])]
        return res