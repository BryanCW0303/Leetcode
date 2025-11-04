class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n-1 and nums[i] < nums[i+1]:
            i += 1
        if i == n-1:
            return n * (n+1) // 2
        j = n-1
        ans = i+2
        while j == n-1 or nums[j] < nums[j+1]:
            while i >= 0 and nums[i] >= nums[j]:
                i -= 1
            ans += i + 2
            j -= 1
        return ans