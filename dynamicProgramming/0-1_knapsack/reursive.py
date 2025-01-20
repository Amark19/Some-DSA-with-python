def knapsack(W, wt, val, n):
    if n == 0:
        if wt[0] <= W:
            return val[0]
        else:
            return 0
    not_take = 0 + knapsack(W, wt, val, n - 1)
    take = float("-inf")
    if wt[n] <= W:
        take = val[n] + knapsack(W - wt[n], wt, val, n - 1)
    return max(not_take, take)


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(W, wt, val, n))  # 220
