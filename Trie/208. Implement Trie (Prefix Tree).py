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

    def find(self, word: str) -> int:
        cur = self.root
        for ch in word:
            if ch not in cur.son:
                return 0
            cur = cur.son[ch]
        return 2 if cur.end else 1

    def search(self, word: str) -> bool:
        return self.find(word) == 2

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) > 0