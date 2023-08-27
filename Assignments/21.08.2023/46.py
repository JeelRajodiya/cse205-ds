from typing import Any, List


class Solution:

    def recursion(self, nums: List[int], mask: List[Any], ans: List[List[int]],
                  it: int):

        if (it == len(nums)):
            ans.append(mask.copy())

        for i in range(0, len(nums)):
            if mask[i] == "X":
                mask[i] = nums[it]
                self.recursion(nums, mask, ans, it + 1)
                mask[i] = "X"

    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        mask = ["X"] * len(nums)
        self.recursion(nums, mask, ans, 0)
        return ans


s = Solution()
print(s.permute([1, 5, 8]))
