from collections import deque
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def check(mid):
            visited = [[False] * n for _ in range(n)]
            if grid[0][0] > mid:
                return False
            if (0, 0) == (n - 1, n - 1):
                return True
            q = deque([(0, 0)])
            visited[0][0] = True
            while q:
                for _ in range(len(q)):
                    i, j = q.popleft()
                    for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] <= mid and not visited[ni][nj]:
                            if ni == n - 1 and nj == n - 1:
                                return True
                            q.append((ni, nj))
                            visited[ni][nj] = True
            return False

        mx = max(x for row in grid for x in row)
        left, right = 0, mx
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left