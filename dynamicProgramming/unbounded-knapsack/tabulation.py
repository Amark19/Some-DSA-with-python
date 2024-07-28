N = 3
W = 50
val = [60, 100, 120]
wt = [10, 20, 30]
dp = [[-1 for _ in range(W + 1)] for _ in range(N)]
for Wt in range(wt[0], W + 1):
    dp[0][Wt] = (Wt // wt[0]) * val[0]
for idx in range(1, N):
    for Wt in range(W + 1):
        take = float("-inf")
        not_take = 0 + dp[idx - 1][Wt]
        if Wt >= wt[idx]:
            take = val[idx] + dp[idx][Wt - wt[idx]]
        dp[idx][Wt] = max(take, not_take)

print(dp[N - 1][W])