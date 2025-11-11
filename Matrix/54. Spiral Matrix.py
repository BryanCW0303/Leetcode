class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        k = 0
        ans = []
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        cnt = 0
        i, j = 0, 0

        def check(i, j, k):
            di, dj = direction[k % 4][0], direction[k % 4][1]
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= m or nj < 0 or nj >= n or visited[ni][nj]:
                return False
            return True

        while cnt < m * n:
            cnt += 1
            visited[i][j] = True
            ans.append(matrix[i][j])
            if not check(i, j, k):
                k += 1
            di, dj = direction[k % 4][0], direction[k % 4][1]
            i, j = i + di, j + dj
        return ans