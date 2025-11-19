from collections import deque

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def check(low):
            fire = deque([])
            on_fire = set()
            for i, row in enumerate(grid):
                for j, x in enumerate(row):
                    if x == 1:
                        fire.append((i, j))
                        on_fire.add((i, j))

            def bfs_fire():
                for _ in range(len(fire)):
                    i, j = fire.popleft()
                    for di, dj in direction:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and (ni, nj) not in on_fire:
                            fire.append((ni, nj))
                            on_fire.add((ni, nj))

            for _ in range(low):
                bfs_fire()
            if (0, 0) in on_fire:
                return False

            people = deque([(0, 0)])
            visited = [[False] * n for _ in range(m)]
            visited[0][0] = True

            while people:
                for _ in range(len(people)):
                    i, j = people.popleft()
                    if (i, j) in on_fire:
                        continue
                    for di, dj in direction:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0 and not visited[ni][nj] and (ni,
                                                                                                          nj) not in on_fire:
                            if ni == m - 1 and nj == n - 1:
                                return True
                            visited[ni][nj] = True
                            people.append((ni, nj))
                bfs_fire()
            return False

        left, right = 0, m * n + 1
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right if right < m * n else 10 ** 9