from itertools import accumulate

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        s = list(accumulate(stations, initial=0))
        power = [s[min(i + r + 1, n)] - s[max(i - r, 0)] for i in range(n)]

        def check(low):
            diff = [0] * n
            sum_d = 0
            built = 0
            for i, x in enumerate(power):
                sum_d += diff[i]
                val = low - (x + sum_d)
                if val <= 0:
                    continue
                built += val
                if built > k:
                    return False
                sum_d += val
                right = i + 2 * r + 1
                if right < n:
                    diff[right] -= val
            return True

        mn = min(power)
        left, right = mn + k // n, mn + k
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right