from math import inf
from typing import List
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in times:
            g[u-1].append((v-1, w))
        dis = [inf] * n
        dis[k-1] = 0
        h = [(0, k-1)]
        while h:
            dx, x = heappop(h)
            if dx > dis[x]:
                continue
            for y, t in g[x]:
                new_dis = dis[x] + t
                if new_dis < dis[y]:
                    dis[y] = new_dis
                    heappush(h, (new_dis, y))
            ans = max(dis)
        return ans if ans < inf else -1