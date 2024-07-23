mod = (int)(1e9 + 7)
arr = [1, 2, 3, 4, 5]
sum = 10
n = len(arr)
dp = [[-1 for _ in range(sum + 1)] for _ in range(n+1)]

##BASE CASE
# If subset sum is 0 that means arr is null
dp[0][0] = 1
# if arr is null then there is no way we can generate sum from 1->sum
for i in range(1, sum + 1):
    dp[0][i] = 0
    for i in range(1, n + 1):
        for j in range(sum + 1):
            not_take = dp[i - 1][j]
        take = 0
        if arr[i - 1] <= j:
            take = dp[i - 1][j - arr[i - 1]]
    dp[i][j] = not_take + take
    # print(dp)
print(dp[n][sum] % mod)