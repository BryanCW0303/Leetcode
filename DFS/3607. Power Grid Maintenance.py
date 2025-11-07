from heapq import heappush, heappop

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        grid_nums = [0] * (c + 1)
        visited = [False] * (c + 1)
        valid = [True] * (c + 1)
        g = [[] for _ in range(c + 1)]
        for u, v in connections:
            g[u].append(v)
            g[v].append(u)
        cnt = 0
        h = []

        def dfs(x):
            visited[x] = True
            heappush(h[-1], x)
            grid_nums[x] = cnt
            for y in g[x]:
                if not visited[y]:
                    dfs(y)

        for i in range(1, c + 1):
            if not visited[i]:
                h.append([])
                dfs(i)
                cnt += 1

        ans = []
        for status, x in queries:
            if status == 1:
                if valid[x]:
                    ans.append(x)
                else:
                    num = grid_nums[x]
                    while h[num] and not valid[h[num][0]]:
                        heappop(h[num])
                    if h[num]:
                        ans.append(h[num][0])
                    else:
                        ans.append(-1)
            if status == 2:
                valid[x] = False
        return ans