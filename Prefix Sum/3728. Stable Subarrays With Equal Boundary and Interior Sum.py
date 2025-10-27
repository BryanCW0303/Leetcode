from collections import defaultdict
from typing import List
from itertools import accumulate

class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        s = list(accumulate(capacity, initial = 0))
        n = len(capacity)
        cnt = defaultdict(int)
        ans = 0
        for right in range(2, n):
            left = right - 2
            x, y = capacity[left], capacity[right]
            cnt[(x + s[left+1], x)] += 1
            ans += cnt[(s[right], y)]
        return ans