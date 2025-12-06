class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        # @cache
        # def dfs(i, d):
        #     if i == n:
        #         return 0 if d == 0 else inf
        #     if d == 0:
        #         return inf
        #     mx = 0
        #     res = inf
        #     for j in range(i, n):
        #         x = jobDifficulty[j]
        #         mx = max(mx, x)
        #         res = min(res, dfs(j+1, d-1) + mx)
        #     return res
        # ans = dfs(0, d)
        # dfs.cache_clear()
        # return ans if ans < inf else -1

        f = [[inf] * (d+1) for _ in range(n+1)]
        f[n][0] = 0
        for i in range(n-1, -1, -1):
            for k in range(d):
                mx = 0
                for j in range(i, n):
                    x = jobDifficulty[j]
                    mx = max(mx, x)
                    f[i][k+1] = min(f[i][k+1], f[j+1][k] + mx)
        ans = f[0][d]
        return ans if ans < inf else -1