def isSubsetSum(self, N, arr, sum):
    # code here
    dp = [[-1 for _ in range(sum + 1)] for _ in range(N)]

    def recur(n, targ):
        if targ == 0: return True
        if n == 0: return (arr[0] == targ)
        if dp[n][targ] != -1: return dp[n][targ]
        not_take = recur(n - 1, targ)
        take = False
        if targ >= arr[n]:
            take = recur(n - 1, targ - arr[n])
        dp[n][targ] = not_take or take
        return dp[n][targ]

    return recur(N - 1, sum)
