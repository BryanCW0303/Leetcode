from functools import cache

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 1_000_000_007

        def calc(num: str):
            high = list(map(int, num))
            n = len(high)

            @cache
            def dfs(i, s, isLimit):
                if s > max_sum:
                    return 0
                if i == len(high):
                    return 1 if s >= min_sum else 0
                res = 0
                up = high[i] if isLimit else 9
                for j in range(up + 1):
                    res = (res + dfs(i + 1, s + j, isLimit and j == up)) % MOD
                return res % MOD

            return dfs(0, 0, True)

        def check(num):
            num = list(map(int, num))
            s = 0
            for x in num:
                s += x
            return min_sum <= s <= max_sum

        return (calc(num2) - calc(num1) + (check(num1))) % MOD