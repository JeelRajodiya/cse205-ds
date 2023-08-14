"""
4
2
1 


8 
4 
2 
1


7
3.5


14
7

"""

import math


class Solution:

    def isPowerOfTwo(self, n: float) -> bool:

        if int(n) == 1:
            return True
        elif n == 0 or n % 2 != 0:
            return False

        return self.isPowerOfTwo(n / 2)


c = Solution()
print(c.isPowerOfTwo(80))