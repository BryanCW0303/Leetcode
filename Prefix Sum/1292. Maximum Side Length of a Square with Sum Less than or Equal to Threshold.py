from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x

        def check(k):
            for r1 in range(m - k + 1):
                for c1 in range(n - k + 1):
                    r2, c2 = r1 + k - 1, c1 + k - 1
                    if s[r2 + 1][c2 + 1] - s[r2 + 1][c1] - s[r1][c2 + 1] + s[r1][c1] <= threshold:
                        return True
            return False

        l, r = 0, min(m, n)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r