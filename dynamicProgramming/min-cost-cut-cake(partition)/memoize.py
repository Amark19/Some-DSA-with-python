class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:

        ## 4D Dp
        dp = [[[[-1 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(m + 1)]

        def recur(starti, endi, startj, endj):
            ## Base Case
            if endi - starti == 1 and endj - startj == 1:
                return 0
            if dp[starti][endi][startj][endj] != -1:
                return dp[starti][endi][startj][endj]
            mn = float("inf")
            for i in range(starti + 1, endi):
                row_val = horizontalCut[i - 1] + recur(starti, i, startj, endj) + recur(i, endi, startj, endj)
                mn = min(mn, row_val)
            for j in range(startj + 1, endj):
                col_val = verticalCut[j - 1] + recur(starti, endi, startj, j) + recur(starti, endi, j, endj)
                mn = min(mn, col_val)
            dp[starti][endi][startj][endj] = mn
            return mn

        return recur(0, m, 0, n)