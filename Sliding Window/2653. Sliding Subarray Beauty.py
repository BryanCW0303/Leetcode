from collections import Counter

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = Counter(nums[: k-1])
        n = len(nums)
        ans = [0] * (n - k + 1)
        for right in range(k-1, n):
            in_ = nums[right]
            cnt[in_] += 1
            left = right - k
            if left >= 0:
                out = nums[left]
                cnt[out] -= 1
            val = x
            for j in range(-50, 0):
                val -= cnt[j]
                if val <= 0:
                    ans[right - k + 1] = j
                    break
        return ans