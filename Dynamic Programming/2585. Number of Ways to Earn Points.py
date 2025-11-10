class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 1_000_000_007

        n = len(types)
        f = [[0] * (target + 1) for _ in range(n+1)]
        f[0][0] = 1

        for i in range(n):
            cnt, mark = types[i][0], types[i][1]
            for j in range(target+1):
                f[i+1][j] = f[i][j]
                max_k = min(cnt, j // mark)
                for k in range(1, max_k+1):
                    f[i+1][j] = (f[i+1][j] + f[i][j - k * mark]) % MOD
        return f[n][target] % MOD