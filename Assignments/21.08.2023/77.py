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

    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(range(1, n + 1))
        arr = list(filter(lambda a: len(a) == k, self.subsets(arr)))
        return arr
