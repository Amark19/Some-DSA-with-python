def isSubsetSum(self, N, arr, sum):
    # code here
    dp = [[0 for _ in range(sum + 1)] for _ in range(N)]
    ## BASE CASE
    for i in range(N):
        dp[i][0] = True
    if arr[0] <= sum:
        dp[0][arr[0]] = True

    ##LOGIC
    for i in range(1, N):
        for j in range(1, sum + 1):
            not_take = dp[i - 1][j]
            take = False
            if j >= arr[i]:
                take = dp[i - 1][j - arr[i]]
            dp[i][j] = not_take or take
    return dp[N - 1][j]