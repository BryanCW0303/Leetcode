class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        h = []
        for i, row in enumerate(heightMap):
            for j, x in enumerate(row):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    h.append((x, i, j))
                    heightMap[i][j] = -1
        heapify(h)

        ans = 0
        while h:
            min_height, i, j = heappop(h)
            for di, dj in (-1, 0), (1, 0), (0, -1), (0, 1):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and heightMap[ni][nj] >= 0:
                    ans += max(min_height - heightMap[ni][nj], 0)
                    heappush(h, (max(min_height, heightMap[ni][nj]), ni, nj))
                    heightMap[ni][nj] = -1
        return ans