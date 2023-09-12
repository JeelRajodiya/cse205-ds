from typing import List
import math


class Solution:

    def getSign(self, num):
        return num // num

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []
        topLim = 0
        bottomLim = len(matrix)
        rightLim = len(matrix[0])
        leftLim = 0
        while rightLim > leftLim and bottomLim > topLim:
            for i in range(leftLim, rightLim):
                ans.append(matrix[topLim][i])
            topLim += 1

            for i in range(topLim, bottomLim):
                ans.append(matrix[i][rightLim - 1])
            rightLim -= 1

            if not (leftLim < rightLim and topLim < bottomLim):
                break
            for i in range(rightLim - 1, leftLim - 1, -1):
                ans.append(matrix[bottomLim - 1][i])
            bottomLim -= 1

            for i in range(bottomLim - 1, topLim - 1, -1):
                ans.append(matrix[i][leftLim])
            leftLim += 1

        return ans


s = Solution()
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(s.spiralOrder(matrix))
