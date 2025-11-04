from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 1_000_000_007
        nums.sort()
        n = len(nums)
        left, right = 0, n-1
        ans = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                ans += (2 ** (right - left)) % MOD
                left += 1
            else:
                right -= 1
        return ans % MOD