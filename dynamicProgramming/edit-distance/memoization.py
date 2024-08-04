class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) - 1
        n = len(word2) - 1
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]

        def recur(i, j):
            if j < 0: return i + 1
            if i < 0:
                return j + 1
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                dp[i][j] = recur(i - 1, j - 1)
                return dp[i][j]
            else:
                dp[i][j] = 1 + min(recur(i - 1, j), recur(i - 1, j - 1), recur(i, j - 1))
                return dp[i][j]

        return recur(m, n)