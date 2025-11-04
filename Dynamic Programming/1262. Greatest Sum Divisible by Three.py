from typing import List
from math import inf

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # n = len(nums)
        # @cache
        # def dfs(i, j):
        #     if i < 0:
        #         return 0 if j == 0 else -inf
        #     x = nums[i]
        #     return max(dfs(i-1, j), dfs(i-1, (j+x) % 3) + x)
        # return dfs(n-1, 0)

        n = len(nums)
        f = [[-inf] * 3 for _ in range(n+1)]
        f[0][0] = 0
        for i, x in enumerate(nums):
            for j in range(3):
                f[i+1][j] = max(f[i][j], f[i][(j+x) % 3] + x)
        return f[n][0]