from sortedcontainers import SortedList
from collections import defaultdict

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = defaultdict(int)
        L = SortedList()
        R = SortedList()
        sum_left = 0

        def add(x: int) -> None:
            if cnt[x] == 0:
                return
            p = (cnt[x], x)
            if L and p > L[0]:
                nonlocal sum_left
                sum_left += p[0] * p[1]
                L.add(p)
            else:
                R.add(p)

        def remove(x: int) -> None:
            if cnt[x] == 0:
                return
            p = (cnt[x], x)
            if p in L:
                nonlocal sum_left
                sum_left -= p[0] * p[1]
                L.remove(p)
            else:
                R.remove(p)

        def L2R() -> None:
            p = L.pop(0)
            nonlocal sum_left
            sum_left -= p[0] * p[1]
            R.add(p)

        def R2L() -> None:
            p = R.pop()
            nonlocal sum_left
            sum_left += p[0] * p[1]
            L.add(p)

        n = len(nums)
        ans = [0] * (n - k + 1)
        for r, in_val in enumerate(nums):
            remove(in_val)
            cnt[in_val] += 1
            add(in_val)

            l = r - k + 1
            if l < 0:
                continue
            if l - 1 >= 0:
                out = nums[l - 1]
                remove(out)
                cnt[out] -= 1
                add(out)

            while R and len(L) < x:
                R2L()

            while len(L) > x:
                L2R()

            ans[l] = sum_left
        return ans