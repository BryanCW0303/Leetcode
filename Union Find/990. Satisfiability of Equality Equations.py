class UnionFind:
    __slots__ = 'p', 'size'

    def __init__(self, n: int):
        self.p = list(range(n))
        self.size = [1] * n

    def find(self, x: int):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def isSame(self, a: int, b: int):
        if self.find(a) == self.find(b):
            return True
        return False

    def union(self, a: int, b: int):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        if self.size[pa] > self.size[pb]:
            self.p[pb] = pa
            self.size[pa] += self.size[pb]
        else:
            self.p[pa] = pb
            self.size[pb] += self.size[pa]
        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for e in equations:
            a, b = ord(e[0]) - ord('a'), ord(e[-1]) - ord('a')
            ch = e[1]
            if ch == '=':
                uf.union(a, b)

        for e in equations:
            a, b = ord(e[0]) - ord('a'), ord(e[-1]) - ord('a')
            if e[1] == '!' and uf.isSame(a, b):
                return False
        return True