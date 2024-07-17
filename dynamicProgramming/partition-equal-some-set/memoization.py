nums = [14, 9, 8, 4, 3, 2]
total_su = sum(nums)


def recur(idx, su):
    if idx < 0: return su == total_su - su
    if dp[idx][su] != -1:
        return dp[idx][su]
    take = recur(idx - 1, su + nums[idx])
    not_take = recur(idx - 1, su)
    dp[idx][su] = take or not_take
    return dp[idx][su]


n = len(nums)
dp = [[-1 for _ in range(total_su + 1)] for _ in range(n)]
print(recur(n - 1, 0))