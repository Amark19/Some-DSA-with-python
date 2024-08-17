class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts_len = len(cuts)
        cuts.insert(0, 0)
        cuts.append(n)
        dp = [[-1 for _ in range(cuts_len + 1)] for _ in range(cuts_len + 1)]
        cuts.sort()

        def recur(start, end):
            if start > end:
                return 0
            mn = 10000000
            if dp[start][end] != -1:
                return dp[start][end]
            for k in range(start, end + 1):
                cost = cuts[end + 1] - cuts[start - 1] + recur(start, k - 1) + recur(k + 1, end)
                mn = min(mn, cost)
            dp[start][end] = mn
            return mn

        return recur(1, cuts_len)