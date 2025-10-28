from functools import cache
from collections import defaultdict
from math import inf

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        @cache
        def dfs(i):
            if i < 0:
                return 0
            res = inf
            mx = 0
            cnt = defaultdict(int)
            for j in range(i, -1, -1):
                cnt[s[j]] += 1
                mx = max(mx, cnt[s[j]])
                if mx * len(cnt) == i - j + 1:
                    res = min(res, dfs(j-1))
            return res + 1
        return dfs(n-1)