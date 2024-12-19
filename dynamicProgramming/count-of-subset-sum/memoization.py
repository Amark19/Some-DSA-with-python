mod = (int)(1e9 + 7)
arr = [1, 2, 3, 4, 5]
sum = 10
n = len(arr)
dp = [[-1 for _ in range(sum + 1)] for _ in range(n)]


def recur(idx, su):
    if idx < 0:
        return su == 0
    if dp[idx][su] != -1: return dp[idx][su]
    not_take = recur(idx - 1, su)
    take = 0
    if arr[idx] <= su:
        take = recur(idx - 1, su - arr[idx])
    dp[idx][su] = not_take + take
    return dp[idx][su] % mod


print(recur(len(arr) - 1, sum))
