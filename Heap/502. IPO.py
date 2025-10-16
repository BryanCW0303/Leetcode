class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        h = [(-p, c) for p, c in zip(profits, capital)]
        heapify(h)
        while k > 0:
            temp = []
            while h and w < h[0][1]:
                temp.append(heappop(h))
            if not h:
                break
            negative_p, c = heappop(h)
            w += -negative_p
            k -= 1
            for p, c in temp:
                heappush(h, (p, c))
        return w