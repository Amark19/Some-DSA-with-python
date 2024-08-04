class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1 for _ in range(len(t))] for _ in range(len(s))]

        def recursive(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == t[j]:
                dp[i][j] = recursive(i - 1, j - 1) + recursive(i - 1, j)
                return dp[i][j]
            else:
                dp[i][j] = recursive(i - 1, j)
                return dp[i][j]

        n = len(s) - 1
        m = len(t) - 1
        return recursive(n, m)