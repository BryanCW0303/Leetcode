from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ans = []
        cnt = defaultdict(str)
        val_to_key = dict()
        for a, b in zip(s, t):
            if b in val_to_key and val_to_key[b] != a:
                return False
            if a in cnt:
                ans.append(cnt[a])
            else:
                ans.append(b)
                cnt[a] = b
                val_to_key[b] = a
        return "".join(ans) == t