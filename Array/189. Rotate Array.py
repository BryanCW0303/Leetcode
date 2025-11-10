class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Solutions 1
        # n = len(nums)
        # k %= n
        # if k:
        #     nums[: ] = nums[-k: ] + nums[: n-k]

        # Solutions 2
        def rev(l: int, r: int):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k %= n
        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)