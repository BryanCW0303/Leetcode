from typing import List
from math import inf
from heapq import heappush, heappop

class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        g = [[] for _ in range(n)]
        for i, (u, v, d) in enumerate(edges):
            g[u].append((v, d, i))
            g[v].append((u, d, i))

        dis = [inf] * n
        dis[0] = 0
        h = [(0, 0)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:
                continue
            for y, d, _ in g[x]:
                new_dis = dx + d
                if new_dis < dis[y]:
                    dis[y] = new_dis
                    heappush(h, (dis[y], y))

        ans = [False] * len(edges)
        if dis[n - 1] == inf:
            return ans

        visited = [False] * n

        def dfs(x: int):
            visited[x] = True
            for y, d, i in g[x]:
                if dis[y] + d == dis[x]:
                    ans[i] = True
                    if not visited[y]:
                        dfs(y)

        dfs(n - 1)
        return ans