from collections import Counter
from string import ascii_lowercase

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        left = Counter(s)
        for ch in target:
            left[ch] -= 1

        ans = list(target)

        for i in range(len(s) - 1, -1, -1):
            ch = target[i]
            left[ch] += 1
            if any(cnt < 0 for cnt in left.values()):
                continue

            for j in range(ord(ch) - ord('a') + 1, 26):
                ch2 = ascii_lowercase[j]
                if left[ch2] == 0:
                    continue

                left[ch2] -= 1
                ans[i] = ch2
                del ans[i + 1:]

                for ch in ascii_lowercase:
                    ans.extend(ch * left[ch])
                return "".join(ans)

        return ""