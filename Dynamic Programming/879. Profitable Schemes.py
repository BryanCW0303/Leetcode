class Solution:
    def profitableSchemes(self, cost: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 1_000_000_007
        n = len(group)

        # @cache
        # def dfs(i, c, p):
        #     if i < 0:
        #         return 1 if c >= 0 and p <= 0 else 0
        #     if group[i] > c:
        #         return dfs(i-1, c, p) % MOD
        #     return (dfs(i-1, c, p) + dfs(i-1, c-group[i], p-profit[i])) % MOD
        # ans = dfs(n-1, cost, minProfit)
        # return ans % MOD

        f = [[[0] * (minProfit + 1) for _ in range(cost + 1)] for _ in range(n + 1)]
        for j in range(cost + 1):
            f[0][j][0] = 1

        for i in range(n):
            c = group[i]
            p = profit[i]
            for j in range(cost + 1):
                for k in range(minProfit + 1):
                    if c > j:
                        f[i + 1][j][k] = f[i][j][k] % MOD
                    else:
                        f[i + 1][j][k] = (f[i][j][k] + f[i][j - c][max(k - p, 0)]) % MOD
        return f[n][cost][minProfit] % MOD