import numpy as np

from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                # save the top left
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move the bottom right into the bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move the top right into the bottom right

                matrix[bottom][r - i] = matrix[top + i][r]

                #move the top left into the top right

                matrix[top + i][r] = topLeft
            r -= 1
            l += 1


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
print(np.array(matrix))

s = Solution()
print(s.rotate(matrix))
