from itertools import combinations

class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 2:
            return 0

        def check(low):
            colors = [0] * n

            def dfs(i, c):
                colors[i] = c
                x1, y1 = points[i]
                for j, (x2, y2) in enumerate(points):
                    if i == j or abs(x1 - x2) + abs(y1 - y2) >= low:
                        continue
                    if colors[j] == c or (colors[j] == 0 and not dfs(j, -c)):
                        return False
                return True

            for i, c in enumerate(colors):
                if colors[i] == 0 and not dfs(i, 1):
                    return False
            return True

        mx = max(abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in combinations(points, 2))
        left, right = 0, mx
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right