def minimizeCost(self, height, n, k):
    dp = [-1 for i in range(n)]
    for i in range(n):
        if i == 0:
            dp[i] = 0
            continue
        mx_steps = float("inf")
        for j in range(1, k + 1):
            if i - j >= 0:
                steps = dp[i - j] + abs(height[i] - height[i - j])
                mx_steps = min(mx_steps, steps)
        dp[i] = mx_steps
    return dp[n - 1]