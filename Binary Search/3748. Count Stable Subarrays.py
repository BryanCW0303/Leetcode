from bisect import bisect_right

class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        s = [0]
        left = []
        start = 0
        i = 0
        while i < n:
            x = nums[i]
            if i == n - 1 or x > nums[i + 1]:
                m = i - start + 1
                s.append(s[-1] + m * (m + 1) // 2)
                left.append(start)
                start = i + 1
            i += 1

        ans = []
        for l, r in queries:
            i = bisect_right(left, l)
            j = bisect_right(left, r) - 1

            if i > j:
                m = r - l + 1
                ans.append(m * (m + 1) // 2)
                continue

            m = left[i] - l
            m2 = r - left[j] + 1
            val1 = m * (m + 1) // 2
            val2 = m2 * (m2 + 1) // 2
            ans.append(val1 + val2 + s[j] - s[i])
        return ans