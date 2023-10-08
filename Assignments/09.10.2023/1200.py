from typing import List


class Solution:

    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        pairs = {}
        prev = 0

        for i in range(1, len(arr)):
            currElem = arr[i]
            prevElem = arr[prev]
            diff = abs(currElem - prevElem)
            if diff in pairs:
                pairs[diff].append([prevElem, currElem])
            else:
                pairs[diff] = [[prevElem, currElem]]
            prev = i
        minDiff = min(list(pairs.keys()))
        return pairs[minDiff]