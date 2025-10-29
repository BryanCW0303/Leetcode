from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        def check(x: int, y: int) -> bool:
            if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
                return True
            return False

        def bothPositive(x: int, y: int) -> bool:
            if x >= 0 and y >= 0:
                return True
            return False

        n = len(nums)

        for i in range(n):
            target[i] -= nums[i]

        ans = abs(target[0])
        for i in range(n - 1):
            x, y = target[i], target[i + 1]
            if check(x, y):
                if bothPositive(x, y):
                    ans += max(y - x, 0)
                else:
                    ans += max(x - y, 0)
            else:
                ans += abs(y)
        return ans