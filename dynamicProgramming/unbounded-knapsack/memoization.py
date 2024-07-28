N = 3
W = 50
val = [60, 100, 120]
wt = [10, 20, 30]
dp = [[-1 for _ in range(W + 1)] for _ in range(N)]


# code here
def recur(idx, Wt):
    if idx == 0:
        if Wt >= wt[0]:
            return (Wt // wt[0]) * val[0]
        else:
            return 0
    if dp[idx][Wt] != -1:
        return dp[idx][Wt]
    take = float("-inf")
    not_take = 0 + recur(idx - 1, Wt)
    if Wt >= wt[idx]:
        take = val[idx] + recur(idx, Wt - wt[idx])
    dp[idx][Wt] = max(take, not_take)
    return dp[idx][Wt]


print(recur(N - 1, W))