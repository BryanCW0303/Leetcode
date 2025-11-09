class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        st = []
        ans = 0
        for i, x in enumerate(nums):
            while st and x < st[-1]:
                ans += 1
                st.pop()
            if not st or x > st[-1]:
                st.append(x)
        return ans + len(st) - (st[0] == 0)