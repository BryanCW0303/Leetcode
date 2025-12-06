class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        max_q = deque()
        min_q = deque()
        f = [0] * (n + 1)
        f[0] = 1
        left = 0
        sum_f = 0
        for i, x in enumerate(nums):
            sum_f += f[i]
            while min_q and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(i)

            while max_q and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(i)

            while nums[max_q[0]] - nums[min_q[0]] > k:
                sum_f -= f[left]
                left += 1
                while min_q[0] < left:
                    min_q.popleft()
                while max_q[0] < left:
                    max_q.popleft()

            f[i + 1] = sum_f % MOD

        return f[n] % MOD