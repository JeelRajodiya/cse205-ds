from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        currSum = 0
        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSum = max(currSum, maxSum)
        return maxSum


s = Solution()
nums = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
print(s.maxSubArray(nums))