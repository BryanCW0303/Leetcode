from functools import cache

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n = str(n)
        digits = set(digits)
        @cache
        def dfs(i, zero, isLimit):
            if i == len(n):
                return 1
            res = 0
            up = int(n[i]) if isLimit else 9
            for j in range(up + 1):
                if j == 0 and zero:
                    res += dfs(i+1, True, False)
                else:
                    if str(j) in digits:
                        res += dfs(i+1, False, isLimit and j == up)
            return res
        return dfs(0, True, True) - 1