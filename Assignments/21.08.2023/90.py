from typing import List


class Solution:

    def recursion(self, nums: List[int], it: int, subSet: List[int],
                  ans: List[List[int]]):
        if it == len(nums):
            if subSet not in ans:
                ans.append(subSet.copy())
            return

        subSet.append(nums[it])
        self.recursion(nums, it + 1, subSet, ans)
        subSet.pop()
        while len(nums) > it + 1 and nums[it] == nums[it + 1]:
            it += 1
        self.recursion(nums, it + 1, subSet, ans)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.recursion(nums, 0, [], ans)
        return ans


s = Solution()
nums = [1, 2, 2]
print(s.subsetsWithDup(nums))