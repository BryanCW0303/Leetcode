from typing import List

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        zero_idx = []
        for i, x in enumerate(arr):
            if x == 0:
                zero_idx.append(i)
        n = len(arr)
        visited = [False] * n
        def dfs(i):
            if i in zero_idx:
                return True
            x = arr[i]
            for sign in [-1, 1]:
                j = i + sign * x
                if j >= 0 and j < n and not visited[j]:
                    visited[j] = True
                    if dfs(j):
                        return True
            return False
        return dfs(start)