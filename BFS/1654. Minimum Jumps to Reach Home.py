from collections import deque
from typing import List

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        s = set(forbidden)
        q = deque([(0, False)])
        visited = {(0, False)}
        step = 0
        while q:
            for _ in range(len(q)):
                i, back = q.popleft()
                if i == x:
                    return step
                if not back:
                    ni = i - b
                    node = (ni, True)
                    if 0 <= ni <= 6000 and ni not in s and node not in visited:
                        q.append(node)
                        visited.add(node)
                ni = i + a
                node = (ni, False)
                if 0 <= ni <= 6000 and ni not in s and node not in visited:
                    q.append(node)
                    visited.add(node)
            step += 1
        return -1