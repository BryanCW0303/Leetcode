class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 1_000_000_007
        s = [0] * (n+1)
        s[1] = 1
        for j in range(2, n+1):
            known = s[max(j-delay, 0)] - s[max(j-forget, 0)]
            s[j] = (s[j-1] + known) % MOD
        return (s[n] - s[max(n-forget, 0)]) % MOD