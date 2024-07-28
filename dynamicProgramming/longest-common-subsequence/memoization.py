text1 = "abcde"
text2 = "ace"

dp = [[-1 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]


def recur(i, j):
    if i < 0 or j < 0: return 0
    if dp[i][j] != -1: return dp[i][j]
    if text1[i] == text2[j]:
        dp[i][j] = 1 + recur(i - 1, j - 1)
        return dp[i][j]
    dp[i][j] = max(recur(i - 1, j), recur(i, j - 1))
    return dp[i][j]


print(recur(len(text1) - 1, len(text2) - 1))