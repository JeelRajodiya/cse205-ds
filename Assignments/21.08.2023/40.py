from typing import Any, List


class Solution:

    def combinationSum2(self, candidates: List[int],
                        target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(it, cur, target):
            if target == 0:
                ans.append(cur.copy())

            if target <= 0:
                return
            prev = -1
            for i in range(it, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                dfs(i + 1, cur, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        dfs(0, [], target)
        return ans


s = Solution()
candidates = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
]
print(s.combinationSum2(candidates, 30))
