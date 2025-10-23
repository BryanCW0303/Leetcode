from functools import cache
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def dfs(i):
            if i >= n-1:
                return True
            for j in range(1, nums[i]+1):
                if dfs(i+j):
                    return True
            return False
        return dfs(0)