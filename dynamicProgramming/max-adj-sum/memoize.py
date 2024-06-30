def FindMaxSum(self, a, n):
    dp = [-1 for i in range(n)]

    def recur(arr, idx):
        if (idx == 0): return arr[idx]
        if (idx < 0): return 0
        if dp[idx] != -1:
            return dp[idx]
        should_consider = arr[idx] + recur(arr, idx - 2)
        not_consider = 0 + recur(arr, idx - 1)
        dp[idx] = max(should_consider, not_consider)
        return dp[idx]

    return recur(a, n - 1)