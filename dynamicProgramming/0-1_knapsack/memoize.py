def knapsack(W, wt, val, n):
    if n==0 or W==0:
        return 0
    if dp[n][W] != -1:
        return dp[n][W]
    if wt[n-1] <= W:
        dp[n][W] = max(val[n-1]+knapsack(W-wt[n-1],wt,val,n-1),
                       knapsack(W,wt,val,n-1))
        return dp[n][W]
    else:
        dp[n][W] = knapsack(W,wt,val,n-1)
        return dp[n][W]

n = 3
W = 50
val = [60, 100, 120]
wt = [10, 20, 30]
dp = [[-1 for _  in range(W+1)] for _ in range(n+1)]
knapsack(W, wt, val, n)