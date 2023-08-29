from typing import List


class Solution:

    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            newArr = list(range(0, len(nums) - 1))
            for n in range(len(newArr)):

                newArr[n] = (nums[n] + nums[n + 1]) % 10
            nums = newArr.copy()

        return nums[0]


s = Solution()
nums = [1, 2, 3, 4, 5]
print(s.triangularSum(nums))
