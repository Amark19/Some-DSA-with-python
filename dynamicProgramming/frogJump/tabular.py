def minimumEnergy(self, height, n):
    dp = [-1 for i in range(n)]
    for i in range(n):
        if i == 0:
            dp[i] = 0
            continue
        left = dp[i - 1] + abs(height[i] - height[i - 1])
        right = float('inf')
        if i > 1:
            right = dp[i - 2] + abs(height[i] - height[i - 2])
        dp[i] = min(left, right)
    return dp[n - 1]