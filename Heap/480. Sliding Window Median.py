from typing import List
from collections import defaultdict
from heapq import heappush, heappop, heappushpop

class LazyHeap:

    def __init__(self):
        self.heap = []
        self.remove_cnt = defaultdict(int)
        self.size = 0

    def remove(self, x: int) -> None:
        self.remove_cnt[x] += 1
        self.size -= 1

    def apply_remove(self) -> None:
        while self.heap and self.remove_cnt[self.heap[0]] > 0:
            self.remove_cnt[self.heap[0]] -= 1
            heappop(self.heap)

    def top(self) -> int:
        self.apply_remove()
        return self.heap[0]

    def pop(self) -> int:
        self.apply_remove()
        self.size -= 1
        return heappop(self.heap)

    def push(self, x: int) -> None:
        heappush(self.heap, x)
        self.size += 1

    def pushpop(self, x: int) -> int:
        self.apply_remove()
        return heappushpop(self.heap, x)


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = LazyHeap()
        right = LazyHeap()
        n = len(nums)
        ans = [0] * (n - k + 1)
        for i, x in enumerate(nums):
            if left.size == right.size:
                left.push(-right.pushpop(x))
            else:
                right.push(-left.pushpop(-x))

            l = i - k + 1
            if l < 0:
                continue
            if k % 2:
                ans[l] = -left.top()
            else:
                ans[l] = (-left.top() + right.top()) / 2

            y = nums[l]
            if y <= -left.top():
                left.remove(-y)
                if left.size < right.size:
                    left.push(-right.pop())
            else:
                right.remove(y)
                if left.size > right.size + 1:
                    right.push(-left.pop())

        return ans