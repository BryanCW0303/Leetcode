class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        ans = s
        n = len(s)
        s = list(s)
        for _ in range(n):
            s = s[-b: ] + s[: -b]
            for _ in range(10):
                for i in range(1, n, 2):
                    s[i] = str((int(s[i]) + a) % 10)
                if b & 1:
                    for _ in range(10):
                        for j in range(0, n, 2):
                            s[j] = str((int(s[j]) + a) % 10)
                        t = "".join(s)
                        if ans > t:
                            ans = t
                else:
                    t = "".join(s)
                    if ans > t:
                        ans = t
        return ans