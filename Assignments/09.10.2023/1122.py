from typing import List


class Solution:

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        idxToNum = {}
        numToIdx = {}
        for n, i in enumerate(arr2):
            idxToNum[n] = i
            numToIdx[i] = n

        sortedArr = []
        arr1Idxes = []
        arrWithoutIdx = []
        for i in arr1:
            idx = numToIdx.get(i)
            if idx == None:
                arrWithoutIdx.append(i)
            else:
                arr1Idxes.append(idx)
        arr1Idxes.sort()
        arrWithoutIdx.sort()
        for i in arr1Idxes:
            sortedArr.append(idxToNum[i])
        sortedArr.extend(arrWithoutIdx)

        return sortedArr