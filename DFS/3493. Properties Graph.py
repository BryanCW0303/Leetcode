from typing import List

class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        def isConnect(a: List[int], b: List[int]):
            if len(set(a) & set(b)) >= k:
                return True
            return False

        def dfs(u):
            if visited[u]:
                return
            visited[u] = True
            for v in edges[u]:
                dfs(v)

        n = len(properties)
        edges = [[] for _ in range(n)]
        for i in range(n):
            p1 = properties[i]
            for j in range(i + 1, n):
                p2 = properties[j]
                if isConnect(p1, p2):
                    edges[i].append(j)
                    edges[j].append(i)

        visited = [False] * n
        ans = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1
        return ans