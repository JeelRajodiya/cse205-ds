import heapq


class Solution:

    def largestInteger(self, num: int) -> int:

        odd_x = []
        even_x = []
        ans = []
        for i in str(num):
            i = int(i)
            if i % 2:
                odd_x.append(-i)
                ans.append(True)
            else:
                even_x.append(-i)
                ans.append(False)

        heapq.heapify(odd_x)
        heapq.heapify(even_x)

        for i in range(len(ans)):
            if ans[i]:
                ans[i] = -heapq.heappop(odd_x)
            else:
                ans[i] = -heapq.heappop(even_x)

        return int("".join(str(n) for n in ans))