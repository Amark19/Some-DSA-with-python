# Function to find the maximum money the thief can get.
def FindMaxSum(self, arr, n):
    dp = [-1 for i in range(n)]
    for idx in range(n):
        if (idx == 0): dp[idx] = arr[idx];continue
        should_consider = arr[idx]
        if idx > 1:
            should_consider += dp[idx - 2]
        not_consider = 0 + dp[idx - 1]
        dp[idx] = max(should_consider, not_consider)
    return dp[n - 1]