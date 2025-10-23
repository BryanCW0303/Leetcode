from functools import cache
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        @cache
        def dfs(i, k):
            if i == n-1:
                return True
            x = stones[i]
            for jump in [k-1, k, k+1]:
                if jump > 0 and x + jump in stones:
                    j = stones.index(x+jump)
                    if dfs(j, jump):
                        return True
            return False
        return dfs(0, 0)