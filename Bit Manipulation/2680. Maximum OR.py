from typing import List

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suf = [0] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] | nums[i + 1]

        ans = 0
        pre = 0
        for x, suf_or in zip(nums, suf):
            ans = max(ans, pre | (x << k) | suf_or)
            pre |= x
        return ans