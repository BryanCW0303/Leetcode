from collections import defaultdict
from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixSum = 0
        cnt = defaultdict(int)
        cnt[0] = -1
        ans = 0
        for i, x in enumerate(nums):
            prefixSum = prefixSum + 1 if x == 1 else prefixSum - 1
            if prefixSum in cnt:
                ans = max(ans, i - cnt[prefixSum])
            else:
                cnt[prefixSum] = i
        return ans