class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0 for _ in range(len(p))] for _ in range(len(s))]

        def recur(i, j):
            if i < 0 and j < 0: return True
            if i < 0 and j >= 0:
                for k in range(j + 1):
                    if p[k] != "*": return False
                return True
            if j < 0 and i >= 0: return False
            if dp[i][j] != 0: return dp[i][j]
            if s[i] == p[j] or p[j] == "?":
                dp[i][j] = recur(i - 1, j - 1)
                return dp[i][j]
            elif p[j] == "*":
                dp[i][j] = recur(i - 1, j) or recur(i, j - 1)
                return dp[i][j]
            return False

        m = len(s) - 1
        n = len(p) - 1
        return recur(m, n)