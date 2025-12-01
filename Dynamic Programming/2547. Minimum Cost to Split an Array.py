class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # @cache
        # def dfs(i):
        #     if i < 0:
        #         return 0
        #     res = inf

        #     s = set()
        #     trim = set()
        #     l = 0
        #     for j in range(i, -1, -1):
        #         x = nums[j]
        #         if x not in s:
        #             s.add(x)
        #         else:
        #             trim.add(x)
        #             l += 1
        #         res = min(res, dfs(j-1) + len(trim) + l + k)

        #     return res
        # return dfs(n-1)

        f = [inf] * (n+1)
        f[0] = 0
        for i in range(n):
            s = set()
            trim = set()
            l = 0
            for j in range(i, -1, -1):
                x = nums[j]
                if x not in s:
                    s.add(x)
                else:
                    trim.add(x)
                    l += 1
                f[i+1] = min(f[i+1], f[j] + len(trim) + l + k)
        return f[n]