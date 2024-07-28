def knapsack(W, wt, val, n):
    if n == 0:
        if wt[0] <= W:
            return val[0]
        else:
            return 0
    if dp[n][W] != -1: return dp[n][W]
    not_take = 0 + knapsack(W, wt, val, n - 1)
    take = float("-inf")
    if wt[n] <= W:
        take = val[n] + knapsack(W - wt[n], wt, val, n - 1)
    dp[n][W] = max(not_take, take)
    return dp[n][W]


n = 3
W = 50
val = [60, 100, 120]
wt = [10, 20, 30]
dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
knapsack(W, wt, val, n)