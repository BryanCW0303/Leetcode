def sign(a, b):
    return (a > b) - (a < b)

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        n = len(str(num2))
        up = list(map(int, str(num2)))
        low = list(map(int, str(num1).zfill(n)))

        @cache
        def dfs(i, cnt, status, pre, lowLimit, upLimit, isNum):
            if i == n:
                return cnt

            lowDigit = low[i] if lowLimit else 0
            upDigit = up[i] if upLimit else 9
            res = 0

            for j in range(lowDigit, upDigit + 1):
                res += dfs(i + 1, cnt + (status * sign(pre, j) == -1), sign(pre, j) if isNum else 0, j,
                           lowLimit and j == lowDigit, upLimit and j == upDigit, isNum or j != 0)
            return res

        return dfs(0, 0, 0, 0, True, True, False)