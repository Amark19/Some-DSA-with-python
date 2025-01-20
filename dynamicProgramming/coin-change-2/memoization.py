# SAME AS MINIMUM COIN CHANGE BUT TO AVOID DUPLICATES WILL HAVE SOME TWEAK TO AVOID DUPLICATES
coins = [1, 2, 5]
amount = 11
dp = [[-1 for _ in range(len(coins))] for _ in range(amount + 1)]
dp[0][0] = 1


def recur(targ, idx):
    if targ == 0:
        return 1
    if targ < 0:
        return 0
    if dp[targ][idx] != -1: return dp[targ][idx]
    mn = 0
    for i in range(idx, len(coins)):
        mn += recur(targ - coins[i], i)
    dp[targ][idx] = mn
    return mn


print(recur(amount, 0))
