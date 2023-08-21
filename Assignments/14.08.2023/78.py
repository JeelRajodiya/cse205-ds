from typing import List

count = 0


class Solution:

    def subs(self, nums: List[int], i: int, tempArr: List[int],
             arr: List[int]):
        global count
        count += 1
        print(f"loop: {count}, i = {i}, tempArr={tempArr}")
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
print(s.subsets([1, 2, 3]))
