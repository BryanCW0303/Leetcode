from collections import defaultdict

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        diff = defaultdict(int)
        for x in nums:
            cnt[x] += 1
            diff[x]
            diff[x - k] += 1
            diff[x + k + 1] -= 1

        ans = 0
        s = 0
        for key, freq in sorted(diff.items()):
            s += freq
            ans = max(ans, min(s, cnt[key] + numOperations))
        return ans