class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dis = [[inf] * (k + 2) for _ in range(n)]
        dis[src][0] = 0
        g = [[] for _ in range(n)]
        for u, v, p in flights:
            g[u].append((v, p))

        h = [(0, src, 0)]
        while h:
            dx, x, edge = heappop(h)
            if edge > k:
                continue
            new_edge = edge + 1
            if dx > dis[x][edge]:
                continue
            for y, dy in g[x]:
                new_dis = dis[x][edge] + dy
                if new_dis < dis[y][new_edge]:
                    dis[y][new_edge] = new_dis
                    heappush(h, (dis[y][new_edge], y, new_edge))
        ans = min(dis[dst])
        return ans if ans < inf else -1