from typing import List
from math import inf
from heapq import heappush, heappop

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 1_000_000_007
        f = [0] * n
        f[0] = 1
        g = [[] for _ in range(n)]
        for u, v, d in roads:
            g[u].append((v, d))
            g[v].append((u, d))

        dis = [inf] * n
        dis[0] = 0
        h = [(0, 0)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:
                continue
            for y, d in g[x]:
                new_dis = dx + d
                if new_dis == dis[y]:
                    f[y] += f[x]
                    f[y] %= MOD
                if new_dis < dis[y]:
                    dis[y] = new_dis
                    heappush(h, (dis[y], y))
                    f[y] = f[x]
        return f[n - 1] % MOD