from typing import List


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        indexMap = {}
        for i in nums:
            if i in indexMap:
                indexMap[i] += 1
            else:
                indexMap[i] = 1

        items = list(map(lambda a: (a[1], a[0]), list(indexMap.items())))
        items.sort()
        items = list(reversed(items))
        ans = []
        print(items)
        for i in range(k):
            ans.append(items[i][1])
        return ans
