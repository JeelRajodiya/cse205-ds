from typing import List


class Solution:

    def subs(self, nums: List[int], i: int, tempArr: List[int],
             arr: List[int]):

        # print(tempArr, i)
        if i == len(nums):
            arr.append(tempArr.copy())
            return

        self.subs(nums, i + 1, tempArr, arr)
        tempArr.append(nums[i])

        self.subs(nums, i + 1, tempArr, arr)
        tempArr.pop()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr = []
        self.subs(nums, 0, [], arr)
        return arr


s = Solution()
print(s.subsets([1, 2, 5, 5]))
