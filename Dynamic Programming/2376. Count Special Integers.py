from functools import cache

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        n = str(n)
        @cache
        def dfs(i, s, zero, isLimit):
            if i == len(n):
                return 1
            up = int(n[i]) if isLimit else 9
            res = 0
            for j in range(up + 1):
                if (s >> j) & 1:
                    continue
                if j == 0 and zero:
                    res += dfs(i+1, s, True, False)
                else:
                    res += dfs(i+1, s | 1 << j, False, isLimit and j == up)
            return res
        return dfs(0, 0, True, True) - 1