N = 3
W = 50
val = [60, 100, 120]
wt = [10, 20, 30]
prev = [0 for _ in range(W + 1)]
for Wt in range(wt[0], W + 1):
    prev[Wt] = (Wt // wt[0]) * val[0]
for idx in range(1, N):
    for Wt in range(W + 1):
        take = float("-inf")
        not_take = 0 + prev[Wt]
        if Wt >= wt[idx]:
            take = val[idx] + prev[Wt - wt[idx]]
        prev[Wt] = max(take, not_take)
print(prev[W])