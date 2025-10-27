from collections import defaultdict
from typing import List

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        prefix_sum = 0
        ans = 0
        last_start = 0
        n = len(nums)
        for i, x in enumerate(nums):
            if i > 0 and x != nums[i-1]:
                y = nums[i-1]
                s = prefix_sum
                for _ in range(i-last_start):
                    cnt[s % k] += 1
                    s -= y
                last_start = i
            prefix_sum += x
            ans += cnt[prefix_sum % k]
        return ans