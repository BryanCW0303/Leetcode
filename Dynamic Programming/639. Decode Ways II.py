class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 1_000_000_007
        n = len(s)
        @cache
        def dfs(i):
            if i < 0:
                return 1
            res = 0
            ch = s[i]
            if ch == "*":
                res += 9 * dfs(i-1)
            elif 0 < int(ch) <= 9:
                res += dfs(i-1)

            if i-1 >= 0:
                pre = s[i-1]
                if pre == '*' and ch == '*':
                    res += 15 * dfs(i-2)
                elif pre == '*':
                    if int(ch) <= 6:
                        res += 2 * dfs(i-2)
                    else:
                        res += dfs(i-2)
                elif ch == '*':
                    if int(pre) == 1:
                        res += 9 * dfs(i-2)
                    if int(pre) == 2:
                        res += 6 * dfs(i-2)
                else:
                    if int(pre) != 0 and 0 < int(pre + ch) <= 26:
                        res += dfs(i-2)
            return res % MOD
        dfs.cache_clear()
        return dfs(n-1)