from typing import List


class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        newMoney = money
        for i in range(2):
            newMoney -= prices[i]
        if newMoney < 0:
            return money
        return newMoney
