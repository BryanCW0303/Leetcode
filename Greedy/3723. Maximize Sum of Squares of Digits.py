class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        if n * 9 < s:
            return ''
        ans = []
        while s > 0:
            digit = min(9, s)
            ans.append(str(digit))
            s -= digit
            n -= 1
        if n > 0:
            ans += ['0'] * n
        return "".join(ans)