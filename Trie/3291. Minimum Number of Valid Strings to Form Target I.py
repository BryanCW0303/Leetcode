from functools import cache
from math import inf
from typing import List

class Node:
    __slots__ = ('son', 'end')

    def __init__(self):
        self.son = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.son:
                cur.son[ch] = Node()
            cur = cur.son[ch]
        cur.end = True

    def longestPrefix(self, word: str, start: int):
        cur = self.root
        length = 0
        for i in range(start, len(word)):
            ch = word[i]
            if ch in cur.son:
                length += 1
                cur = cur.son[ch]
            else:
                break
        return length


class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        trie = Trie()
        for word in words:
            trie.insert(word)

        @cache
        def dfs(i):
            if i >= n:
                return 0
            length = trie.longestPrefix(target, i)
            if length == 0:
                return inf
            res = inf
            for j in range(1, length + 1):
                res = min(res, dfs(i + j) + 1)
            return res

        return dfs(0) if dfs(0) < inf else -1