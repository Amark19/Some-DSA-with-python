coins = [1, 2, 5]
amount = 11

dp = [float("inf") for _ in range(amount + 1)]
dp[0] = 0
for i in range(1, amount + 1):
    mn = float("inf")
    for j in range(len(coins)):
        if i >= coins[j]:
            mn = min(mn, 1 + dp[i - coins[j]])
    dp[i] = mn
print(dp[amount] if dp[amount] != float("inf") else -1)