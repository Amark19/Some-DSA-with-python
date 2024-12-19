def minimumEnergy(self, height, n):
    dp = [-1 for i in range(n)]

    def somfun(height, i):
        if i == 0:
            return 0
        if dp[i] != -1:
            return dp[i]
        left = somfun(height, i - 1) + abs(height[i] - height[i - 1])
        right = float('inf')
        if i > 1:
            right = somfun(height, i - 2) + abs(height[i] - height[i - 2])
        dp[i] = min(left, right)
        return dp[i]

    return somfun(height, n - 1)
