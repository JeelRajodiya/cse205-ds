from typing import List


class Solution:

    def rev(self, s: List[str], n):
        if n >= (len(s) // 2) or (n % 2 != 0 and n == (len(s) // 2 + 1)):
            return s
        print(n)
        a = s[n]
        b = s[-1 * (n + 1)]
        s[n] = b
        s[-1 * (n + 1)] = a

        return self.rev(s, n + 1)

    def reverseString(self, s: List[str]) -> None:
        s = self.rev(s, 0)
        print(s)


s = Solution()
s.reverseString(["h", "e", "l", "l", "o"])
