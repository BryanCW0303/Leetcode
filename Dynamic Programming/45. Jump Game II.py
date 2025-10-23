from functools import cache
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(i):
            if i >= n-1:
                return 0
            res = inf
            for j in range(1, nums[i]+1):
                res = min(res, dfs(i+j))
            return res + 1
        return dfs(0)