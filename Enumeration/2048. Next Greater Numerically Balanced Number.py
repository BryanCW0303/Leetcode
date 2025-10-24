from itertools import permutations
from bisect import bisect_right

BALANCED = [1, 22, 333, 4444, 55555, 666666]

class Solution:
    def perm(self, s: str):
        perms = set(permutations(s))

        result = sorted([''.join(p) for p in perms])

        for r in result:
            BALANCED.append(int(r))

    def nextBeautifulNumber(self, n: int) -> int:
        self.perm("122")
        self.perm("1333")
        self.perm("14444")
        self.perm("22333")
        self.perm("155555")
        self.perm("122333")
        self.perm("224444")
        self.perm("1224444")
        BALANCED.sort()
        idx = bisect_right(BALANCED, n)
        return BALANCED[idx]