class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 1_000_000_007
        n = len(s)
        # @cache
        # def dfs(i):
        #     if i == n:
        #         return 1
        #     res = 0

        #     if int(s[i]) == 0:
        #         return res

        #     sum_ = 0
        #     for j in range(i, n):
        #         val = int(s[j])
        #         sum_ = 10 * sum_ + val
        #         if sum_ > k:
        #             break
        #         res += dfs(j+1)
        #     return res % MOD
        # dfs.cache_clear()
        # return dfs(0)

        f = [0] * (n+1)
        f[n] = 1
        for i in range(n-1, -1, -1):
            if int(s[i]) == 0:
                continue
            sum_ = 0
            for j in range(i, n):
                val = int(s[j])
                sum_ = 10 * sum_ + val
                if sum_ > k:
                    break
                f[i] = (f[i] + f[j+1]) % MOD
        return f[0]