class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [1] * n
        for i, x in enumerate(ratings):
            left = ratings[i - 1] if i - 1 >= 0 else x
            right = ratings[i + 1] if i + 1 < n else x
            if x < left and ans[i - 1] <= ans[i]:
                ans[i - 1] = ans[i] + 1
            if x < right and ans[i + 1] <= ans[i]:
                ans[i + 1] = ans[i] + 1

        for i in range(n - 1, -1, -1):
            x = ratings[i]
            left = ratings[i - 1] if i - 1 >= 0 else x
            right = ratings[i + 1] if i + 1 < n else x
            if x < left and ans[i - 1] <= ans[i]:
                ans[i - 1] = ans[i] + 1
            if x < right and ans[i + 1] <= ans[i]:
                ans[i + 1] = ans[i] + 1

        return sum(ans)