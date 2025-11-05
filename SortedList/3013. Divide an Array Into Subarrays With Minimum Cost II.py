from sortedcontainers import SortedList

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        k -= 1
        sum_left = sum(nums[: dist + 2])
        L = SortedList(nums[1: dist + 2])
        R = SortedList()

        def L2R():
            nonlocal sum_left
            x = L.pop()
            sum_left -= x
            R.add(x)

        def R2L():
            nonlocal sum_left
            x = R.pop(0)
            sum_left += x
            L.add(x)

        while len(L) > k:
            L2R()

        ans = sum_left
        n = len(nums)
        for i in range(dist + 2, n):
            in_val, out = nums[i], nums[i - dist - 1]
            if out in L:
                sum_left -= out
                L.remove(out)
            else:
                R.remove(out)

            if in_val < L[-1]:
                sum_left += in_val
                L.add(in_val)
            else:
                R.add(in_val)

            while len(L) > k:
                L2R()
            while R and len(L) < k:
                R2L()

            ans = min(ans, sum_left)
        return ans