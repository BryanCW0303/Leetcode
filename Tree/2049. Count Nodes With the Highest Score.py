from collections import defaultdict
from typing import List

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        children = defaultdict(list)
        for i in range(1, n):
            children[parents[i]].append(i)

        ans = 0
        mx = -inf

        def dfs(i):
            nonlocal ans, mx
            s = 0
            p = 1
            for j in children[i]:
                val = dfs(j)
                s += val
                if val > 0:
                    p *= val
            remain = n - 1 - s
            if remain > 0:
                p *= remain
            if p > mx:
                mx = p
                ans = 1
            elif p == mx:
                ans += 1
            return s + 1

        dfs(0)
        return ans