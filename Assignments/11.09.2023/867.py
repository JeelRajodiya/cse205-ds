from typing import List
import numpy as np

import numpy as np


class Solution:

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        resultArr = list(np.zeros([len(matrix[0]), len(matrix)],
                                  dtype="int32"))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):

                resultArr[j][i] = matrix[i][j]
        return list(map(lambda a: list(a), resultArr))


s = Solution()
mat = [[1, 2, 3], [4, 5, 6]]

print(s.transpose(mat))
