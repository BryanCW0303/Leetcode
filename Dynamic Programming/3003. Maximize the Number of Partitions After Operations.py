class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def dfs(i, mask, changed):
            if i == len(s):
                return 1

            res = 0
            bit = 1 << ord(s[i]) - ord('a')
            new_mask = mask | bit
            if new_mask.bit_count() > k:
                res = max(res, dfs(i + 1, bit, changed) + 1)
            else:
                res = max(res, dfs(i + 1, new_mask, changed))
            if changed:
                return res

            for j in range(26):
                new_mask = mask | (1 << j)
                if new_mask.bit_count() > k:
                    res = max(res, dfs(i + 1, 1 << j, True) + 1)
                else:
                    res = max(res, dfs(i + 1, new_mask, True))
            return res

        return dfs(0, 0, False)