from functools import cache

class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        @cache
        def dfs(i, zero, isLimit):
            if i == len(s):
                return 1
            res = 0
            up = int(s[i]) if isLimit else 9
            for j in range(up + 1):
                if j == 0:
                    if zero:
                        res += dfs(i+1, True, False)
                else:
                    res += dfs(i+1, False, isLimit and j == up)
            return res
        return dfs(0, True, True) - 1