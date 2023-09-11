from typing import List


class Solution:

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sums = []
        for i in accounts:
            sums.append(sum(i))
        return max(sums)
