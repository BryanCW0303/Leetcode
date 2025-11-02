from typing import List
from math import lcm

class Solution:
    def minimumTime(self, d: List[int], r: List[int]) -> int:
        def check(time):
            return time - time // r[0] >= d[0] and time - time // r[1] >= d[1] and time - time // lcm(r[0], r[1]) >= d[
                0] + d[1]

        left, right = 1, 1
        while not check(right):
            right *= 2

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left