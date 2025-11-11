from math import inf
from heapq import heappush, heappop

class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)
        g = [[] for _ in range(n)]
        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))
        dis = [[inf] * (maxTime + 1) for _ in range(n)]
        dis[0][0] = 0
        h = [(0, 0, 0)]
        while h:
            dx, x, time = heappop(h)
            if dx > dis[x][time]:
                continue
            for y, dt in g[x]:
                new_time = time + dt
                if new_time > maxTime:
                    continue
                new_dis = dis[x][time] + passingFees[x]
                if new_dis < dis[y][new_time]:
                    dis[y][new_time] = new_dis
                    heappush(h, (new_dis, y, new_time))
        ans = min(dis[n-1])
        return ans + passingFees[n-1] if ans < inf else -1