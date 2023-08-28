class Solution:

    def findKthPositive(self, arr, k):
        fq = {}
        for num in arr:
            if num in fq:
                fq[num] += 1
            else:
                fq[num] = 1

        ans = 0
        for i in range(1, 10001):
            if i not in fq:
                k -= 1
            if k == 0:
                ans = i
                break

        return ans