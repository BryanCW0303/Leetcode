class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        right = n-1
        while right and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:
            return 0
        ans = right
        left = 0
        while True:
            while right == n or arr[left] <= arr[right]:
                ans = min(ans, right - left - 1)
                if arr[left] > arr[left + 1]:
                    return ans
                left += 1
            right += 1
        return ans