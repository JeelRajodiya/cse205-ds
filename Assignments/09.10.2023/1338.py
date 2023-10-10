from collections import defaultdict
from typing import List


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        freqMap = {}

        for i in arr:
            if i in freqMap:
                freqMap[i] += 1
            else:
                freqMap[i] = 1

        mulMap = defaultdict(list)
        for i in freqMap:
            mulMap[freqMap[i]].append(i)

        myset = {}
        count = 0
        n = len(arr)
        sum = len(arr)
        print(mulMap)
        reversedKeys = list(sorted(mulMap.keys(), reverse=True))

        for i in reversedKeys:
            for j in mulMap[i]:
                count += 1
                sum -= i
                # print(sum,n,i)
                if sum <= n / 2:
                    return count
        return 0
