from typing import List
from itertools import accumulate

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def check(k):
            diff = [0] * len(nums)
            diff[0] = nums[0]
            for i in range(1, len(nums)):
                diff[i] = nums[i] - nums[i - 1]
            for i in range(k):
                l, r, val = queries[i]
                diff[l] -= val
                if r + 1 < len(nums):
                    diff[r + 1] += val
            return all(x <= 0 for x in list(accumulate(diff)))

        n = len(queries)
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if not check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return l if l <= n else -1