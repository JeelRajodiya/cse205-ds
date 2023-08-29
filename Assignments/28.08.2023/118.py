from typing import List, Any


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:

        triangle: List[Any] = list(range(0, numRows))
        for i in range(0, numRows):

            triangle[i] = list(range(0, i + 1))
            triangle[i][0] = 1
            triangle[i][-1] = 1

            for j in range(0, i - 1):

                print(triangle[i], i, j)

                triangle[i][j +
                            1] = triangle[i - 1][j] + triangle[i - 1][j + 1]

        return triangle


s = Solution()
print(s.generate(5))
