from collections import defaultdict, deque
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        n = len(arr)

        val_to_idxs = defaultdict(list)
        for i, x in enumerate(arr):
            val_to_idxs[x].append(i)

        visited = [False] * n
        visited[0] = True
        q = deque([0])
        step = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()
                val = arr[i]
                for j in val_to_idxs[val]:
                    if 0 <= j < n and not visited[j]:
                        if j == n-1:
                            return step + 1
                        visited[j] = True
                        q.append(j)
                del val_to_idxs[val]
                for j in [i-1, i+1]:
                    if 0 <= j < n and not visited[j]:
                        if j == n-1:
                            return step + 1
                        visited[j] = True
                        q.append(j)
            step += 1