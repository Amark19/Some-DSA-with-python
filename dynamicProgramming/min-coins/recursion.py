coins = [1, 2, 5]
amount = 11


def recur(targ):
    if targ == 0:
        return 0
    if targ < 0:
        return float("inf")
    mn = float("inf")
    for i in range(len(coins)):
        mn = min(mn, 1 + recur(targ - coins[i]))
    return mn


ans = recur(amount)
if ans == float("inf"):
    print(-1)
print(ans)