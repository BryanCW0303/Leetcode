from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        if endWord not in s:
            return 0

        s.add(beginWord)

        g = defaultdict(list)
        for word in s:
            for i in range(len(word)):
                for j in range(26):
                    new_word = word[: i] + chr(ord("a") + j) + word[i + 1:]
                    if new_word != word and new_word in s:
                        g[word].append(new_word)

        q = deque([(beginWord, 1)])
        visited = set()
        visited.add(beginWord)
        while q:
            for _ in range(len(q)):
                word, step = q.popleft()
                if word == endWord:
                    return step
                for new_word in g[word]:
                    if new_word not in visited:
                        q.append((new_word, step + 1))
                        visited.add(new_word)
        return 0