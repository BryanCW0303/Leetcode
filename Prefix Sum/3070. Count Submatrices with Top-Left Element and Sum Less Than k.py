from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        s = [[0] * (n+1) for _ in range(m+1)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + x
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i][j] <= k:
                    ans += 1
        return ans