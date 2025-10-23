from typing import List

class UnionFind:
    __slots__ = 'p', 'size'

    def __init__(self, n: int):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a: int, b: int):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pb] += self.size[pa]
        else:
            self.p[pa] = pb
            self.size[pa] += self.size[pb]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for a, b in edges:
            if not uf.union(a - 1, b - 1):
                return [a, b]
        return []