def knapsack(W, wt, val, n):
    for Wt in range(wt[0],W):dp[0][Wt] = val[0]
    for i in range(1,n):
        for Wt in range(1,W):
            not_take = 0 + dp[i-1][Wt]
            take = float("-inf")
            if wt[i] <= Wt:
                take = val[n] + dp[i-1][Wt - wt[i]]
            dp[i][Wt] = max(not_take, take)
    return dp[n-1][W]


n = 3
W = 50
val = [60, 100, 120]
wt = [10, 20, 30]
dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
knapsack(W, wt, val, n)