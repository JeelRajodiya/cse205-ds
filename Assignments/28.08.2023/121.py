from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowPrice = prices[0]
        if not prices:
            return 0
        for price in prices:
            if price < lowPrice:
                lowPrice = price
            else:
                maxProfit = max(maxProfit, price - lowPrice)

        return maxProfit


s = Solution()
prices = [7, 1, 5, 3, 6, 4]

print(s.maxProfit(prices))