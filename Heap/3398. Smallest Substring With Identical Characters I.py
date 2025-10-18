from heapq import heapreplace, heapify

class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)
        cnt = sum((ord(b) ^ i) & 1 for i, b in enumerate(s))
        if min(cnt, n - cnt) <= numOps:
            return 1

        g = (list(t) for _, t in groupby(s))
        h = [(-k, k, 1) for k in map(len, g)]
        heapify(h)

        while numOps > 0:
            k, l, seg = h[0]
            if k == -2:
                return 2
            else:
                new_k = -(l // (seg + 1))
                heapreplace(h, (new_k, l, seg + 1))
            numOps -= 1
        return -h[0][0]