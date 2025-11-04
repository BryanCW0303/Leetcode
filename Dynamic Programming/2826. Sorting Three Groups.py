from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # LIS
        # n = len(nums)
        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     res = 0
        #     for j in range(i-1, -1, -1):
        #         if nums[j] <= nums[i]:
        #             res = max(res, dfs(j))
        #     return res + 1
        # return n - max(dfs(i) for i in range(n))

        n = len(nums)
        f = [[0] * 4 for _ in range(n+1)]
        for i, x in enumerate(nums):
            for j in range(1, 4):
                if x <= j:
                    f[i+1][j] = max(f[i][j], f[i][x] + 1)
                else:
                    f[i+1][j] = f[i][j]
        return n - f[n][3]