from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cnt = defaultdict(int)
        k = 0
        ans = []
        for word in strs:
            temp = list(word)
            temp.sort()
            key = "".join(temp)
            if key in cnt:
                ans[cnt[key]].append(word)
            else:
                cnt[key] = k
                ans.append([word])
                k += 1
        return ans