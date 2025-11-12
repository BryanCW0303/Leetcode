from functools import cache

class Solution:
    def findIntegers(self, n: int) -> int:
        bit = bin(n)[2: ]
        k = n.bit_length()
        @cache
        def dfs(i, preOne, isLimit):
            if i == k:
                return 1
            up = int(bit[i]) if isLimit else 1
            res = 0
            for j in range(up + 1):
                if preOne and j == 1:
                    continue
                res += dfs(i+1, j == 1, isLimit and j == up)
            return res
        return dfs(0, False, True)