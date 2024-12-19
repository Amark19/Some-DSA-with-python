def minimizeCost(self, height, n, k):
    dp = [-1 for i in range(n)]

    def somfun(height, i, k):
        if i == 0:
            return 0
        mx_steps = float("inf")
        for j in range(1, k + 1):
            if i - j >= 0:
                steps = somfun(height, i - j, k) + abs(height[i] - height[i - j])
                mx_steps = min(mx_steps, steps)
        return mx_steps

    return somfun(height, n - 1, k)
