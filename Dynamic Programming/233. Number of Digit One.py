from functools import cache

class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        @cache
        def dfs(i, cnt, isLimit):
            if i == len(s):
                return cnt
            up = int(s[i]) if isLimit else 9
            res = 0
            for j in range(up+1):
                res += dfs(i+1, cnt + (j == 1), isLimit and j == up)
            return res
        return dfs(0, 0, True)