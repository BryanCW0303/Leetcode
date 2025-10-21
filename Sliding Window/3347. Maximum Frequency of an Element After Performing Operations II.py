class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        n = len(nums)
        cnt = left = right = 0
        ans = 0
        for i, x in enumerate(nums):
            cnt += 1
            if i < n - 1 and nums[i + 1] == x:
                continue
            while nums[left] < x - k:
                left += 1
            while right < n and nums[right] <= x + k:
                right += 1
            ans = max(ans, min(right - left, cnt + numOperations))
            cnt = 0

        if ans >= numOperations:
            return ans

        left = 0
        for right, x in enumerate(nums):
            while nums[left] < x - 2 * k:
                left += 1
            ans = max(ans, right - left + 1)
        return min(ans, numOperations)