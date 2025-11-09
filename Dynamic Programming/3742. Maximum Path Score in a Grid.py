from math import inf

class Solution:
    def maxPathScore(self, grid: List[List[int]], K: int) -> int:
        m, n = len(grid), len(grid[0])
        f = [[[-inf] * (K + 2) for _ in range(n + 1)] for _ in range(m + 1)]
        f[0][1][1:] = [0] * (K + 1)

        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                for k in range(K + 1):
                    new_k = k - 1 if x else k
                    f[i + 1][j + 1][k + 1] = max(f[i][j + 1][new_k + 1], f[i + 1][j][new_k + 1]) + x
        ans = f[m][n][-1]
        return ans if ans >= 0 else -1