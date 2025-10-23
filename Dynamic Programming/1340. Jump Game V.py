from functools import cache
from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        @cache
        def dfs(i):
            left = arr[i-1] if i-1 >= 0 else inf
            right = arr[i+1] if i+1 < n else inf
            x = arr[i]
            if x <= left and x <= right:
                return 1
            res = 0
            for j in range(1, d+1):
                if i+j >= n or arr[i+j] >= x:
                    break
                res = max(res, dfs(i+j))
            for j in range(1, d+1):
                if i-j < 0 or arr[i-j] >= x:
                    break
                res = max(res, dfs(i-j))
            return res + 1
        return max(dfs(i) for i in range(n))