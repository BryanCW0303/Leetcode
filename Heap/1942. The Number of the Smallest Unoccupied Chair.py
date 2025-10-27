from typing import List
from heapq import heappush, heappop

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        idx = sorted(range(n), key = lambda i: times[i][0])
        start = 0
        heap = []
        available = []
        for i in idx:
            arrival, leaving = times[i]
            while heap and arrival >= heap[0][0]:
                _, released_chair = heappop(heap)
                heappush(available, released_chair)
            if available:
                chair = heappop(available)
            else:
                chair = start
                start += 1
            if i == targetFriend:
                return chair
            heappush(heap, (leaving, chair))