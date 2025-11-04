class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len(s)
        # @cache
        # def dfs(i, c, state):
        #     if c == 0:
        #         return 1
        #     if i < 0:
        #         return 0
        #     if int(s[i]) != state:
        #         return dfs(i-1, c, state)
        #     else:
        #         return dfs(i-1, c-1, 1-state) + dfs(i-1, c, state)
        # return dfs(n-1, 3, 1) + dfs(n-1, 3, 0)

        f = [[0] * 2 for _ in range(4)]
        f[0][0] = f[0][1] = 1
        for x in s:
            for c in range(3, 0 , -1):
                if x == '0':
                    f[c][1] += f[c-1][0]
                else:
                    f[c][0] += f[c-1][1]
        return f[3][0] + f[3][1]